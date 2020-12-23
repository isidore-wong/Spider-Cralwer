# --*-- coding:utf-8 --*--
import redis
from random import choice

'''
@File: db.py
@Author: Hayes Wong
@Email: 616132717@qq.com
@Time:  2020-12-16 10:31
'''

'''
https://github.com/Python3WebSpider/ProxyPool
代理池分为 4 个模块：存储模块、获取模块、检测模块、接口模块。
 - 存储模块使用 Redis 的有序集合，用来做代理的去重和状态标识，同时它也是中心模块和基础模块，将其他模块串联起来。
 - 获取模块定时从代理网站获取代理，将获取的代理传递给存储模块，并保存到数据库。
 - 检测模块定时通过存储模块获取所有代理，并对代理进行检测，根据不同的检测结果对代理设置不同的标识。
 - 接口模块通过 Web API 提供服务接口，接口通过连接数据库并通过 Web 形式返回可用的代理。
'''

'''
首先我们定义了一些常量，如 MAX_SCORE、MIN_SCORE、INITIAL_SCORE 分别代表最大分数、最小分数、初始分数。
REDIS_HOST、REDIS_PORT、REDIS_PASSWORD 分别代表了 Redis 的连接信息，即地址、端口、密码。REDIS_KEY 是有序集合的键名，
我们可以通过它来获取代理存储所使用的有序集合。

接下来定义了一个 RedisClient 类，这个类可以用来操作 Redis 的有序集合，其中定义了一些方法来对集合中的元素进行处理，它的主要功能如下所示。

* __init__()方法是初始化的方法，其参数是 Redis 的连接信息，默认的连接信息已经定义为常量，在__init__() 
方法中初始化了一个 StrictRedis 的类，建立 Redis 连接。
* add() 方法向数据库添加代理并设置分数，默认的分数是 INITIAL_SCORE 也就是 10，返回结果是添加的结果。
* random() 方法是随机获取代理的方法，首先获取 100 分的代理，然后随机选择一个返回。如果不存在 100 分的代理，则此方法按照排名来获取，
选取前 100 名，然后随机选择一个返回，否则抛出异常。
* decrease() 方法是在代理检测无效的时候设置分数减 1 的方法，代理传入后，此方法将代理的分数减 1，如果分数达到最低值，那么代理就删除。
* exists() 方法可判断代理是否存在集合中。
* max() 方法将代理的分数设置为 MAX_SCORE，即 100，也就是当代理有效时的设置。
* count() 方法返回当前集合的元素个数。
* all() 方法返回所有的代理列表，供检测使用。
'''

MAX_SCORE = 100
MIN_SCORE = 0
INITIAL_SCORE = 10
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_PASSWORD = None
REDIS_KEY = 'proxies'

class RedisClient(object):
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD):
        """
        初始化
        :param host: Redis 地址
        :param port: Redis 端口
        :param password: Redis 密码
        """
        self.db = redis.StrictRedis(host=host, port=port, password=password, decode_responses=True)

    def add(self, proxy, score=INITIAL_SCORE):
        """
        添加代理，设置分数为最高
        :param proxy: 代理
        :param score: 分数
        :return: 添加结果
        """
        if not self.db.zscore(REDIS_KEY, proxy):
            return self.db.zadd(REDIS_KEY, score, proxy)

    def random(self):
        """
        随机获取有效代理，首先尝试获取最高分数代理，如果不存在，按照排名获取，否则异常
        :return: 随机代理
        """
        result = self.db.zrangebyscore(REDIS_KEY, MAX_SCORE, MAX_SCORE)
        if len(result):
            return choice(result)
        else:
            result = self.db.zrevrange(REDIS_KEY, 0, 100)
            if len(result):
                return choice(result)
            # else:
            #    raise PoolEmptyError

    def decrease(self, proxy):
        """
        代理值减一分，小于最小值则删除
        :param proxy: 代理
        :return: 修改后的代理分数
        """
        score = self.db.zscore(REDIS_KEY, proxy)
        if score and score > MIN_SCORE:
            print(' 代理 ', proxy, ' 当前分数 ', score, ' 减 1')
            return self.db.zincrby(REDIS_KEY, proxy, -1)
        else:
            print(' 代理 ', proxy, ' 当前分数 ', score, ' 移除 ')
            return self.db.zrem(REDIS_KEY, proxy)

    def exists(self, proxy):
        """
        判断是否存在
        :param proxy: 代理
        :return: 是否存在
        """
        return not self.db.zscore(REDIS_KEY, proxy) == None

    def max(self, proxy):
        """
        将代理设置为 MAX_SCORE
        :param proxy: 代理
        :return: 设置结果
        """
        print(' 代理 ', proxy, ' 可用，设置为 ', MAX_SCORE)
        return self.db.zadd(REDIS_KEY, MAX_SCORE, proxy)

    def count(self):
        """
        获取数量
        :return: 数量
        """
        return self.db.zcard(REDIS_KEY)

    def all(self):
        """
        获取全部代理
        :return: 全部代理列表
        """
        return self.db.zrangebyscore(REDIS_KEY, MIN_SCORE, MAX_SCORE)

# _*_ coding:utf-8 _*_


"""
@version: python 3.6
@author: Isidore
@contact: 616132717@qq.com
@time: 2019/12/24 22:58
"""

"""
程序目的：定义采集到的口碑数据

"""
class AutohomeItem(object):
    # 结构化数据--评论类数据
    space_score = None              # 空间评分
    power_score = None              # 动力评分
    maneuverability_score = None    # 操控性得分
    oil_score = None                # 油耗评分
    comfortableness_score = None    # 舒适性评分
    apperance_score = None          # 外观评分
    internal_score = None           # 内饰得分
    costefficient_score = None      # 性价比评分
    Satisfaction = None             # 满意度--以上8项用户的综合平均分

    # 半结构化数据
    user_id = None                  # 车主ID
    brand_name = None               # 车系名称--轩逸/天籁等
    spec_name = None                # 车型型号--如2020款 1.6L XL CVT智享版
    city_name = None                # 城市名称
    bought_dlr = None               # 购买经销商
    buy_date = None                 # 购买日期
    buy_price = None                # 购买价格
    purpose = None                  # 购车目的/用途

    content_title = None            # 帖子标题
    pub_date = None                 # 帖子发布日期
    review_levels = None            # 帖子等级
    visit_count = None              # 浏览量
    content_url = None              # 内容URL存储表

    # 文本类数据
    car_merit = None                # 车辆优点
    car_defect = None               # 车辆缺陷
    space_feeling = None            # 空间感受
    power_feeling = None            # 动力感受
    maneuverability_feeling = None  # 操控性感受
    oil_feeling = None              # 油耗感受
    comfortableness_feeling = None  # 舒适性感受
    apperance_feeling = None        # 外观感受
    internal_feeling = None         # 内饰感受
    costefficient_feeling = None    # 性价比感受
    bought_reason = None            # 购买原因


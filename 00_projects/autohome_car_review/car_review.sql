drop database if exists `car_review_db`;
create database if not exists `car_review_db`;
use `car_review_db`;

drop table if exists `review_url_tb`;
drop table if exists `review_content_tb`;

# storage reviews content urls
create table if not exists `review_url_tb`(
	`post_id` int auto_increment not null comment '帖子id',
    `content_url` varchar(255) not null comment '帖子内容URL',
    primary key(`post_id`)
)auto_increment = 1;

# storage record which is the review of car
create table if not exists `review_content_tb`(
    `post_id` int primary key auto_increment not null comment '帖子id',
    `content_title` varchar(32) not null comment '帖子标题',
    `pub_date` date not null comment  '发帖时间',
    `review_level` varchar(32) comment '帖子级别',
    `visit_count` int not null comment '浏览量',
    `user_id` varchar(32) comment '车主ID',
    `brand_name` varchar(32) comment '车系名',
    `spec_name` varchar(32) comment '车型',
    `city_name` varchar(32) comment '购买城市',
    `bought_dlr` varchar(32) comment '购车经销商',
    `bought_date` varchar(32) comment '购买日期',
    `bought_price` varchar(32) comment '购买价格',
    `purpose` varchar(32) comment '购车目的',
    
    `space_score` decimal(10,2) comment '空间评分',
    `power_socre` decimal(10,2) comment '动力评分',
    `maneuverability_score` decimal(10,2) comment '操控评分',
    `oil_socre` decimal(10,2) comment '油耗评分',
    `comfortableness_score` decimal(10,2) comment '舒适性评分',
    `apperance_socre` decimal(10,2) comment '外观评分',
    `internal_score` decimal(10,2) comment '内饰评分',
    `costefficient_score` decimal(10,2) comment '性价比评分',
    `Satisfaction` decimal(10,2) comment '综合评分',
    
    `car_merit` varchar(255) comment '车辆优点',
    `car_defect` varchar(255) comment '车辆缺点',
    `space_feeling` varchar(255) comment '空间感受',
    `power_feeling` varchar(255) comment '动力感受',
    `maneuverability_feeling` varchar(255) comment '操控感受',
    `oil_feeling` varchar(255) comment '油耗感受',
    `comfortableness_feeling` varchar(255) comment '舒适性感受',
    `apperance_feeling` varchar(255) comment '外观感受',
    `internal_feeling` varchar(255) comment '内饰感受',
    `costefficient_feeling` varchar(255) comment '性价比感受',
    `bought_reason` varchar(255) comment '购买原因'
)auto_increment = 1;


select * from `review_url_tb`;
select * from `review_content_tb`;
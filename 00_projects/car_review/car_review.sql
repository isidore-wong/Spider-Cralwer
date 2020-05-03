drop database if exists `car_review_db`;
create database if not exists `car_review_db`;
use `car_review_db`;

# storage record which is the review of car
create table if not exists `review_tb`(
    `post_id` varchar(32) primary key not null comment '帖子id',
    `post_name` varchar(32) not null comment '发帖人',
    `pub_time` date not null comment  '发帖时间',
    `review_level` varchar(32) comment '口碑级别',
    `visit_count` int not null comment '浏览量',
    `series_id` varchar(32) comment '车系id',
    `series_name` varchar(32) comment '车系名',
    `spec_name` varchar(32) comment '车型',
    `bought_address` varchar(32) comment '购买地点',
    `bought_dlr` varchar(32) comment '购车经销商',
    `space_score` decimal(10,2) comment '空间评分',
    `power_socre` decimal(10,2) comment '动力评分',
    `maneuverability_score` decimal(10,2) comment '操控评分',
    `oil_socre` decimal(10,2) comment '油耗评分',
    `comfortableness_score` decimal(10,2) comment '舒适性评分',
    `apperance_socre` decimal(10,2) comment '外观评分',
    `internal_score` decimal(10,2) comment '内饰评分',
    `costefficient_score` decimal(10,2) comment '性价比评分',
    `purpose` varchar(32) comment '购车目的',
    `car_merit` varchar(50) comment '车辆优点',
    `car_defect` varchar(50) comment '车辆缺点',
    `space_feeling` varchar(50) comment '空间感受',
    `power_feeling` varchar(50) comment '动力感受',
    `maneuverability_feeling` varchar(50) comment '操控感受',
    `oil_feeling` varchar(50) comment '油耗感受',
    `comfortableness_feeling` varchar(50) comment '舒适性感受',
    `apperance_feeling` varchar(50) comment '外观感受',
    `internal_feeling` varchar(50) comment '内饰感受',
    `costefficient_feeling` varchar(50) comment '性价比感受',
    `bought_reason` varchar(50) comment '购买原因'
);

# storage url of review
create table if not exists `review_url`(
	`post_id` varchar(32) primary key not null comment '帖子id',
    `post_name` varchar(32) not null comment '发帖人',
    `pub_time` date not null comment '发帖时间',
    `post_url` varchar(50) not null comment '帖子URL'
);

select * from `review_tb`;
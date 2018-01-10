# 爱卡汽车论坛信息抓取

## 项目需求

1. 抓取爱卡汽车论坛数据（奔腾x40）并存入mysql数据库
2. 使用结巴分词对文本进行分词
3. 统计mysql数据库数据，并存入mysql数据库

## 推荐环境

- anaconda 1.6.5
- selenium
- chrome
- chromedriver
- pymysql

## 爬虫与数据库表设计

![数据表设计](https://github.com/xiaofang-git/xcar/blob/master/png/%E5%AD%90%E8%AE%BA%E5%9D%9B(%E5%A5%94%E8%85%BEx40).png)

## 爬虫项目结构

1. 修改setting文件数据库连接的配置信息
2. 创建数据库
    - `create database xcar`
3. 创建数据表
    1. `use xcar`
    2. """ sql
    CREATE TABLE `item` (
  `item_id` int(11) NOT NULL,
  `title` char(100) DEFAULT NULL,
  `poster` char(30) DEFAULT NULL,
  `post_time` float DEFAULT NULL,
  `replies` int(11) DEFAULT NULL,
  `view_count` int(11) DEFAULT NULL,
  PRIMARY KEY (`item_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""
    3.

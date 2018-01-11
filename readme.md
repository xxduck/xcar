# 爱卡汽车论坛信息抓取

## 项目需求

1. 抓取爱卡汽车论坛数据（奔腾x40）并存入mysql数据库
2. 使用结巴分词对文本进行分词
3. 统计mysql数据库数据，并存入mysql数据库

## 项目环境

- anaconda（1.6.5开发包）
- selenium（python第三方库）
- chrome（浏览器）
- chromedriver（chrome自动化插件）
- pymysql（python第三方库）
- MySQL（数据库）
- jieba（python第三方库）

## 爬虫与数据库表设计

![数据表设计](https://github.com/xiaofang-git/xcar/blob/master/png/%E5%AD%90%E8%AE%BA%E5%9D%9B(%E5%A5%94%E8%85%BEx40).png)

## 运行项目

1. `git clone https://github.com/xiaofang-git/xcar.git` 下载项目到本地环境
2. 启动python虚拟环境（如果有的话）
3. `pip install jieba selenium pymysql` 安装第三方依赖
4. 添加chromedriver.exe所在目录到系统环境变量（chromedriver.exe在项目根文件下的script文件夹下)
5. 修改setting文件数据库连接的配置信息,以及需要开启的线程数量
6. 创建数据库以及表（以下命令在数据库客户端中运行）
    1. `create database xcar` 创建数据库
    2. `use xcar` 切换数据库到xcar
    3. 创建item表，存放列表页信息
    ```sql
    CREATE TABLE `item` (`item_id` int(11) NOT NULL, `title` char(100) DEFAULT NULL,  `poster` char(30) DEFAULT NULL,  `post_time` float DEFAULT NULL,  `replies` int(11) DEFAULT NULL,  `view_count` int(11) DEFAULT NULL,  PRIMARY KEY (`item_id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    ```
    4. 创建reply表，存放所有回帖信息
    ```sql
    CREATE TABLE `reply` (  `id` int(11) NOT NULL AUTO_INCREMENT,  `item_id` int(11) DEFAULT NULL,  `reply_er` char(30) DEFAULT NULL,  `reply_time` float DEFAULT NULL,  `reply` text,  PRIMARY KEY (`id`)) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;
    ```
    
7. `python main.py` 运行爬虫

## 进度
- [x] 项目设计
- [x] 论坛列表页爬虫
- [x] 论坛帖子回复页爬虫
- [x] 总爬虫入口
- [ ] 单元测试
- [ ] 项目优化重构
- [ ] 数据分析

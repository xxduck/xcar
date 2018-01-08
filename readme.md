# 爱卡汽车论坛信息抓取

## 项目需求

1. 抓取爱卡汽车论坛数据（奔腾x40）并存入mysql数据库
2. 使用结巴分词对文本进行分词
3. 统计mysql数据库数据，并存入mysql数据库

## 推荐环境

- anaconda 1.6.5

## 爬虫与数据库表设计

![数据表设计](xcar/png/子论坛(奔腾x40).png)

## 爬虫项目结构

- 爬虫 `spider`
    - 论坛列表页(贴子摘要页) `abstract.py`
    - 回帖页(贴子详情页) `datail.py`

- 自然语言分析 `analysis`

- 数据库交互 `sql`
    - `sql.py`

- 配置文件
    - `setting.py`

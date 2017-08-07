# Alarm for Aliyun CMS

## v1: python alarm.py

* 非常驻，定时每分钟执行一次
* 警报存在延迟
* 最简单，配置 config.py 即可

## v1: python alarm-realtime.py

* 常驻
* 警报几乎不存在延迟
* 配置稍微麻烦，利用了警报的订阅机制，需配置与授权队列服务(MNS)


## Refs:

* 查询报警历史 https://help.aliyun.com/document_detail/51916.html
* slacker https://github.com/os/slacker
* aliyun-openapi-python-sdk https://github.com/aliyun/aliyun-openapi-python-sdk/tree/master/aliyun-python-sdk-cms/aliyunsdkcms/request/v20170301

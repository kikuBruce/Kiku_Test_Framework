# Kiku_Test_Framework

## 关于

基于Python3的自动化测试框架；  

## 目录结构

```
Kiku_Test_Framework
    |--config
        |--config.yml # 默认的配置文件，写法遵循yaml规范，用于定义常规变量
    |--data
    |--drivers
    |--log
    |--report
    |--test_case # 测试用例
    |--common
        |--file_reader.py # 通过yaml封装方法，读取config.config.yml，返回data，供config.py使用
        |--config.py # 通过调用file_reader，提供方法获取config.config.yml中的具体数据，以字典的形式
        |--log.py # 封装longging，返回log操作句柄
```



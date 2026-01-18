<!--
 * @Descripttion: 
 * @Version: 1.0
 * @Author: WangZhen
 * @Date: 2024-12-12 9:30:47
 * @LastEditors: WangZhen
-->
# Weather-Warning-System

#### 项目简介
​
> 本项目为数据库开发实践大作业：航空天气预警管理系统， 基于[Flask](https://github.com/pallets/flask)框架+MySQL数据库开发，轻量简洁。

#### 项目模块及功能介绍

本系统包括登录模块、注册模块、旅客用户模块、机场人员用户模块、系统管理员模块。具体功能介绍如下:  

+ 登录模块  


+ 注册模块 


+ 旅客用户模块 


+  机场人员用户模块 


+ 系统管理员模块


#### 项目结构
├── static&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//网页静态资源    
│   ├── css&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//css样式配置   
│   ├── fonts&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//字体配置    
│   ├── images&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//图片文件    
│   ├── js&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//javascript脚本文件    
├── templates&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//HTML模板文件    
├── app.py&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//Web服务启动程序    
└── README.md&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//help    

#### 环境依赖

+ Python 3.10
+ Flask 2.4.2
+ PyMySQL 1.0.2  
+ MySQL 8.4

#### 运行方法
找到app.py文件中的以下代码部分，取消注释，并修改MySQL的root用户登录密码，然后执行Web服务启动程序。
if __name__ == '__main__':

    # with app.app_context():
    #     db.create_all()  # 创建数据库表
    #     insert_data()  # 插入数据

    args = parse_args()
    mysql_pwd = args.mysql_pwd
    db_name = args.db_name
    app.run(host='localhost', port='4090')

再执行Web服务启动程序，在终端中输入以下命令，在浏览器中输入`http://localhost:4090`即可访问系统。
~~~python
python app.py --mysql_pwd 0728 --db_name weather_system
~~~
注意此处`mysql_pwd`也是你MySQL的root用户登录密码，`db_name`即models.py文件创建的数据库名称。

#### 系统部分界面展示

### 自用连接数据库驱动模块

- Mysql
- Oracle
- MongoDB

#### 使用方法

1. 配置config.json

   ```json
   {
     "mysql": {
       "host": "",
       "port": "",
       "user": "",
       "password": "",
       "db": "",
       "charset": "utf8"
     },
     "oracle": {
       "host": "",
       "port": "",
       "user": "",
       "password": "",
       "service_name": ""
     },
     "mongodb": {
       "host": "",
       "port": "",
       "user": "",
       "password": "",
       "service_name": ""
     }
   }
   ```

2. ```python
   from Dblogin.login import Login
   
   login = Login()
   client = login.Mysql.conn # 获取mysql连接对象
   ```

3. 后续可以针对不同连接数据库对象添加不同方法

   1. Dblogin/modules/Login.py下 写了三种类
      1. 添加search
      2. 添加update....
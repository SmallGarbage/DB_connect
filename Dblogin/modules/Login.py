import json

import pymysql
import cx_Oracle as cx
import pymongo


class MysqlClient:
    def __init__(self, path=os.path.dirname(__file__) + "/config.json"):
        self.path = path
        self.__initial()

    def __initial(self):
        with open(self.path, "r") as f:
            data = json.loads(f.read())
        self.user = data["mysql"]["user"]
        self.password = data["mysql"]["password"]
        self.host = data["mysql"]["host"]
        self.port = data["mysql"]["port"]
        self.db = data["mysql"]["db"]
        self.charset = data["mysql"]["charset"]
        conn = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db, charset=self.charset)
        self.conn = conn


class OracleClient:
    def __init__(self, path=os.path.dirname(__file__) + "/config.json"):
        self.path = path
        self.__initial()

    def __initial(self):
        with open(self.path, "r") as f:
            data = json.loads(f.read())
        self.user = data["oracle"]["user"]
        self.password = data["oracle"]["password"]
        self.host = data["oracle"]["host"]
        self.port = data["oracle"]["port"]
        self.service_name = data["oracle"]["service_name"]
        conn = cx.connect(self.user, self.password, "{}:{}/{}".format(self.host, self.port, self.service_name))
        self.conn = conn


class MongodbClient:
    def __init__(self, path="./config.json"):
        self.path = path
        self.__initial()

    def __initial(self):
        with open(self.path, "r") as f:
            data = json.loads(f.read())
        self.user = data["mongodb"]["user"]
        self.password = data["mongodb"]["password"]
        self.host = data["mongodb"]["host"]
        self.port = data["mongodb"]["port"]
        self.service_name = data["mongodb"]["service_name"]
        conn = pymongo.MongoClient(f'mongodb://{self.user}:{self.password}@{self.host}:{self.port}')
        self.conn = conn


if __name__ == '__main__':
    pass

import warnings
from modules.Login import MysqlClient, MongodbClient, OracleClient

warnings.filterwarnings('ignore')


class Login(object):
    def __init__(self, disable_print_introduce=True, **kwargs):
        if disable_print_introduce: print(self)
        self.supported_apis = {
            'Mysql': MysqlClient,
            'Oracle': OracleClient,
            'Mongodb': MongodbClient,
        }

        for key, value in self.supported_apis.items():
            setattr(self, key, value)

    def __str__(self):
        return "welcome to use Dblogin!"


if __name__ == '__main__':
    login = Login()
    client = login.Mysql().conn

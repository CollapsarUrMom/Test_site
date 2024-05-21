import json


# Напишите определение класса AppConfig
class AppConfig:

    @classmethod
    def load_config(cls, database):
        with open('C:\\Users\\Alex_job\\Documents\\Git\\Test_site\\app_config.json') as database:
            cls.data = json.load(database)
            return cls.data
        
    @classmethod
    def get_config(cls, k : int = None):
        key = k.split('.')
        print(key)
        if len(key) == 1:
            return cls.data[key[0]]
        elif len(key) == 2:
            print(key)
            print(key[0])
            print(type(key))
            print(type(key[0]))
            return cls.data.get(key[0]key[1], None)



# Загрузка конфигурации при запуске приложения
AppConfig.load_config('app_config.json')

# Получение значения конфигурации
assert AppConfig.get_config('database') == {
    'host': '127.0.0.1', 'port': 5432,
    'database_name': 'postgres_db',
    'user': 'owner',
    'password': 'ya_vorona_ya_vorona'}
assert AppConfig.get_config('database.user') == 'owner'
assert AppConfig.get_config('database.password') == 'ya_vorona_ya_vorona'
assert AppConfig.get_config('database.pass') is None
assert AppConfig.get_config('password.database') is None

config = AppConfig()
assert config.get_config('max_connections') == 10
assert config.get_config('min_connections') is None

conf = AppConfig()
assert conf.get_config('max_connections') == 10
assert conf.get_config('database.user') == 'owner'
assert conf.get_config('database.host') == '127.0.0.1'
assert conf.get_config('host') is None

print('Good')
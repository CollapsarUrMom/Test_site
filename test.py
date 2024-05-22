import json


# Напишите определение класса AppConfig
class AppConfig:

    @classmethod
    def load_config(cls, database) -> dict:
        with open('app_config.json') as database:
            cls.data = json.load(database)
            return cls.data


    @classmethod
    def get_config(cls, key : str = None):
        keys = key.split('.')
        if len(keys) == 1:
            return cls.data.get(keys[0], None)
        elif len(keys) == 2:
            key_1 = cls.data.get(keys[0], None)
            if key_1 is not None:
                return key_1.get(keys[1], None)
            else:
                return None



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
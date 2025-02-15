from motor import motor_asyncio

from settings import settings


class Database:
    db = None

    def __init__(self, url):
        self.url = url
        self.db_name = url.split('/')[-1]

    def initialize(self, loop):
        client = motor_asyncio.AsyncIOMotorClient(self.url, io_loop=loop)
        self.db = client[self.db_name]

    def __getattr__(self, item):
        return getattr(self.db, item)

    def __getitem__(self, item):
        return self.db[item]


MONGO_HOST = settings.get('mongo', {}).get('db_host', '127.0.0.1')
MONGO_PORT = settings.get('mongo', {}).get('db_port', 27017)
MONGO_DATABASE = settings.get('mongo', {}).get('db_database', 'testdb')

db = Database(f'mongodb://{MONGO_HOST}:{MONGO_PORT}/{MONGO_DATABASE}')

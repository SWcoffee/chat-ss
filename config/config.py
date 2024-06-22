import os
import redis

AUTH_KEY = os.getenv('AUTH_KEY', "test")

REDIS_HOST = os.getenv('REDIS_HOST', "localhost")
REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))
REDIS_DB = int(os.getenv('REDIS_DB', 0))

REDIS_CON = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)



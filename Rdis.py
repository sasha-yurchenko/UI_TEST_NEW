import redis

r = redis.Redis(host='d-redis.spacemir.int', port=6379, db=0)
r.flushdb()


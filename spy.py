#!/usr/bin/env python
import redis
import time

# 'host': '172.17.0.2'
config = {
    'host': '10.0.0.1'

}

r = redis.StrictRedis(**config)
pubsub = r.pubsub()
pubsub.psubscribe("*")
for msg in pubsub.listen():
    print time.time(), msg

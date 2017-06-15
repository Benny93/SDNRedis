#!/usr/bin/env python
import redis
import time

config = {
    'host': '172.17.0.2'

}

r = redis.StrictRedis(**config)
pubsub = r.pubsub()
pubsub.psubscribe("*")
for msg in pubsub.listen():
    print time.time(), msg

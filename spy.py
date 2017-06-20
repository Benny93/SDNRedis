#!/usr/bin/env python
import rediscluster
import time

# Requires at least one node for cluster discovery. Multiple nodes is recommended.
startup_nodes = [{"host": "10.0.0.1", "port": "7000"}, {"host": "10.0.0.1", "port": "7001"}]

r = rediscluster.StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)
pubsub = r.pubsub()
# pattern subscription
pubsub.psubscribe("*")
for msg in pubsub.listen():
    print time.time(), msg

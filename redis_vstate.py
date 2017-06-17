"""
Virtual State for SDN implemented with REDIS

"""
import redis


class State(object):
    config = {
        'host': '10.0.0.1',
        'port': '7002'
    }

    def __init__(self):
        # connect to session
        self.redis = redis.StrictRedis(**self.config)

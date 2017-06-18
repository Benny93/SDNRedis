"""
Virtual State for SDN implemented with REDIS

"""
import rediscluster


class State(object):
    OBJECT_IDENTIFIER = 'switch'
    FIELD_IDENTIFIER = 'mac_to_port'

    startup_nodes = [{"host": "10.0.0.1", "port": "7000"}]

    def __init__(self):
        # connect to session
        self.redis = \
            rediscluster.StrictRedisCluster(startup_nodes=self.startup_nodes, decode_responses=True)

    def get_mac_to_port(self, dpid):
        """
        Returns a the mac to port dictionary for switch with
        :param dpid: datapath id of the switch
        :return: dictionary
        """
        name = "{}:{}:{}".format(self.OBJECT_IDENTIFIER, dpid, self.FIELD_IDENTIFIER)
        # if there is no entry for this name, return empty dict
        if not self.redis.exists(name):
            return {}
        # else return the whole dictionary
        return self.redis.hgetall(name)

    def update_mac_to_port(self, dpid, data):
        """

        :param dpid: datapath id of the switch
        :param data: updated dictionary
        :return: dictionary
        """
        name = "{}:{}:{}".format(self.OBJECT_IDENTIFIER, dpid, self.FIELD_IDENTIFIER)
        self.redis.hmset(name, data)

"""
Virtual State for SDN implemented with REDIS

"""
import rediscluster


class State(object):
    OBJECT_IDENTIFIER = 'switch'
    FIELD_IDENTIFIER = 'mac_to_port'

    # TODO: change __init__ signature to require this setting
    # Requires at least one node for cluster discovery. Multiple nodes is recommended.
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
        mac_to_port = self.redis.hgetall(name)
        # convert port back to int
        return dict((mac, int(port)) for (mac, port) in mac_to_port.iteritems())

    def update_mac_to_port(self, dpid, data):
        """

        :param dpid: datapath id of the switch
        :param data: updated dictionary
        :return: dictionary
        """
        name = "{}:{}:{}".format(self.OBJECT_IDENTIFIER, dpid, self.FIELD_IDENTIFIER)
        self.redis.hmset(name, data)

#!/usr/bin/env python
import random
import unittest
from unittest import TestCase

import time


class TestState(TestCase):
    def test_get_mac_to_port(self):
        import redis_vstate as rvs
        state = rvs.State()
        random_dpid = random.randint(12345670, 123456789)
        random_mac = "ca:ff:ee:%02x:%02x:%02x" % (random.randint(0, 255), random.randint(0, 255),
                                                  random.randint(0, 255))
        random_port = random.randint(0, 255)
        my_dict = state.get_mac_to_port(random_dpid)
        my_dict[random_mac] = random_port
        state.update_mac_to_port(random_dpid, my_dict)
        my_dict = state.get_mac_to_port(random_dpid)
        # delete dpid entry
        state.expire_datapath(random_dpid, 1)
        self.assertDictContainsSubset({random_mac: random_port}, my_dict)

    def test_update_mac_to_port(self):
        self.assert_(True)

    def test_expire(self):
        import redis_vstate as rvs
        state = rvs.State()
        dpid = 123456789012340
        my_dict = {'00:00:00:00:00:00': 2}
        state.update_mac_to_port(dpid, my_dict)
        state.expire_datapath(dpid, 1)
        time.sleep(1)
        self.assertDictEqual(state.get_mac_to_port(dpid), {}, "Dictionary for Key should be empty")

        # Running Tests


if __name__ == '__main__':
    unittest.main()

import unittest
from unittest import TestCase


class TestState(TestCase):
    def test_get_mac_to_port(self):
        import redis_vstate as rvs
        state = rvs.State()
        dpid = 123456789012340
        my_dict = state.get_mac_to_port(dpid)
        my_dict['00:00:00:00:00:00'] = 2
        state.update_mac_to_port(dpid, my_dict)
        my_dict = state.get_mac_to_port(dpid)
        self.assertDictContainsSubset({'00:00:00:00:00:00': 2}, my_dict)

    def test_update_mac_to_port(self):
        self.assert_(True)


# Running Tests
if __name__ == '__main__':
    unittest.main()

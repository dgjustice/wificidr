from ipaddress import ip_address, ip_network
import unittest
import logging
import sys
import random
from ipv6gen import IPv6Gen

lazy = False


class IPv6Tests(unittest.TestCase):

    def setUp(self):
        self.log = logging.getLogger()
        self.log.setLevel(logging.DEBUG)
        self.stream_handler = logging.StreamHandler(sys.stderr)
        self.log.addHandler(self.stream_handler)
        self.log.debug("\nSetting up")
        a = hex(random.randrange(0xffff))[2::]
        b = hex(random.randrange(0xffff))[2::]
        self.nets_list = ip_network("2000:{0}:{1}::/48".format(a, b)).subnets(new_prefix=52)

    def tearDown(self):
        self.log.removeHandler(self.stream_handler)

    # Test failures once since sanity checked in class init
    def test_fail52_52left(self):
        with self.assertRaises(ValueError) as e:
            alloc = IPv6Gen("2000:1c0:72:8000::/52", 52)
            gen_nets = alloc.left()
            next(gen_nets)
        exc = e.exception
        self.assertIsInstance(exc, ValueError)

    @unittest.expectedFailure
    def test_fail51_52left(self):
        alloc = IPv6Gen("2000:32:abcd:8000::/52", 51)
        gen_nets = alloc.left()
        next(gen_nets)
        self.assertEqual("foo", "foo")


    # ############### LEFT ############### #
    def test_net48to52left(self):
        self.log.debug("""\nTest /48 split into /52's left""")
        alloc = IPv6Gen("2ab0:1c0e:7dc2::/48", 52)
        gen_nets = alloc.left()
        self.assertEqual(len([i for i in gen_nets]), 16)

    def test_net52to64left(self):
        self.log.debug("""\nTest /52 split into /64's, left""")
        alloc = IPv6Gen("20a0:dd0:beef:8000::/52", 64)
        gen_nets = alloc.left()
        self.assertEqual(len([i for i in gen_nets]), 4096)

    @unittest.skipIf(lazy, "We are lazy")
    def test_net_list_left(self):
        for net in self.nets_list:
            self.log.debug("Testing {} left".format(net))
            alloc = IPv6Gen(net, 64)
            gen_nets = alloc.left()
            self.assertEqual(len([i for i in gen_nets]), 4096)

    # ############### RIGHT ############### #
    def test_net48to52right(self):
        self.log.debug("""\nTest /48 split into /52's right""")
        alloc = IPv6Gen("2000:face:b000::/48", 52)
        gen_nets = alloc.right()
        self.assertEqual(len([i for i in gen_nets]), 16)

    def test_net52to64right(self):
        self.log.debug("""\nTest /52 split into /64's right""")
        alloc = IPv6Gen("22ff:ffff:ffff:8000::/52", 64)
        gen_nets = alloc.right()
        self.assertEqual(len([i for i in gen_nets]), 4096)

    @unittest.skipIf(lazy, "We are lazy")
    def test_net_list_right(self):
        for net in self.nets_list:
            self.log.debug("Testing {} right".format(net))
            alloc = IPv6Gen(net, 64)
            gen_nets = alloc.right()
            self.assertEqual(len([i for i in gen_nets]), 4096)

    # ############### CENTER ############### #
    def test_net48to52center(self):
        self.log.debug("""\nTest /48 split into /52's center""")
        alloc = IPv6Gen("2000:adf:2232::/48", 52)
        gen_nets = alloc.center()
        self.assertEqual(len([i for i in gen_nets]), 16)

    def test_net52to64center(self):
        self.log.debug("""\nTest /52 split into /64's center""")
        alloc = IPv6Gen("2000:ccaf:af39::/52", 64)
        gen_nets = alloc.center()
        self.assertEqual(len([i for i in gen_nets]), 4096)

    @unittest.skipIf(lazy, "We are lazy")
    def test_net_list_center(self):
        for net in self.nets_list:
            self.log.debug("Testing {} center".format(net))
            alloc = IPv6Gen(net, 64)
            gen_nets = alloc.center()
            self.assertEqual(len([i for i in gen_nets]), 4096)

if __name__ == '__main__':
    unittest.main()

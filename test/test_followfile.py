import unittest
import tempfile, os
from openbsd.followfile import *

class uFollowFile(unittest.TestCase):
    def setUp(self):
        self.fname = tempfile.mktemp()
        f = open(self.fname, "w+")
        f.write("some\ninfo")
        f.close()

    def tearDown(self):
        os.unlink(self.fname)

    def test_follow(self):
        for i in followFile(self.fname, timeout=0.0001):
            pass

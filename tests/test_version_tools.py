import unittest

from version_tools.version_helper import bump_version

class TestHelper(unittest.TestCase):
    def test_version_bump(self):
        ver = "0.1.0"
        self.assertEqual(bump_version(ver, "major"), "1.0.0")

        self.assertEqual(bump_version(ver, "minor"), "0.2.0")

        self.assertEqual(bump_version(ver, "patch"), "0.1.1")

        self.assertEqual(str(bump_version(ver, "pre")), "0.1.0-rc.1")

        self.assertEqual(bump_version(ver, "dev"), "0.1.0-dev0")

        ver = "0.1.0-dev0"
        self.assertEqual(str(bump_version(ver, "pre")), "0.1.0-dev1")

        self.assertEqual(bump_version(ver, "final"), "0.1.0")



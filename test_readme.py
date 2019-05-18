import unittest
import glob
import os

os.chdir("./")


class ReadmeTest(unittest.TestCase):

    def test_readme(self):
        for name in glob.glob("./README.md"):
            self.assertEqual(name, "./README.md")


if __name__ == "__main__":
    unittest.main()

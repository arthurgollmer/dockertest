import unittest
from my_script import out

class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual("Pipeline done....", out("Pipeline done...."))


if __name__ == '__main__':
    unittest.main()

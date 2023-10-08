import unittest
from unittest import TestCase
import arraysort


class Test(TestCase):
    def test_zerosort(self):  # test name should start with 'test_'
        sample_array = [1, 0, 0, 1]
        result = arraysort.zerosort(sample_array)
        self.assertEqual(result, [0, 0, 1, 0])


if __name__ == '__main__':
    unittest.main()

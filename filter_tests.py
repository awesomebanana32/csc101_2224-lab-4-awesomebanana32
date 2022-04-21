import unittest
import filter
import point
import math
import typing

class TestCases(unittest.TestCase):

    # input: self
    # result: assert  all positive numbers
    def test_are_positive(self):
        listpositive = [1,3,2]
        list6 = filter.are_positive(listpositive)
        print(list6)
        self.assertEqual(list6, [1,3,2])

    # input: self
    # result: assert all positive numbers
    def test_are_positive_again(self):
        listpositive = [100,3,-2]
        list6 = filter.are_positive(listpositive)
        print(list6)
        self.assertEqual(list6, [100,3])

    # input: self
    # result: assert all numbers greater than n
    def test_are_greater_than(self):
        listn = [100,3,-2]
        list7 = filter.are_greater_than(listn, 5)
        print(list7)
        self.assertEqual(list7, [100])

    # input: self
    # result: assert all numbers greater than n
    def test_are_greater_than_again(self):
        listn = [50,12,42]
        list7 = filter.are_greater_than(listn, 1)
        print(list7)
        self.assertEqual(list7, [50,12,42])

    # input: self
    # result: assert all points that are in the positive quadrant
    def test_are_in_positive_quadrant(self):
        listpoint = [point.Point(-3, 4), point.Point(6, 8), point.Point(8, 15)]
        list5 = filter.are_in_positive_quadrant(listpoint)
        print(list5)
        self.assertEqual(list5, [point.Point(6, 8), point.Point(8, 15)])

    # input: self
    # result: assert all points that are in the positive quadrant
    def test_are_in_positive_quadrant_again(self):
        listpoint = [point.Point(0, 0), point.Point(60, 80), point.Point(82, 15)]
        list5 = filter.are_in_positive_quadrant(listpoint)
        print(list5)
        self.assertEqual(list5, [point.Point(60, 80), point.Point(82, 15)])

# Run the unit tests.
if __name__ == '__main__':
    unittest.main()

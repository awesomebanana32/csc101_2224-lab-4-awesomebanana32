import unittest
import map
import point
import math
import typing


class TestCases(unittest.TestCase):
    # input: self
    # result: assert square of all numbers in a list
    def test_square_all(self):
        listsquare = [1, 2, 3]
        list2 = map.square_all(listsquare)
        print(list2)
        self.assertEqual(list2,[1, 4, 9])

    # input: self
    # result: assert square of all numbers in a list
    def test_square_all_again(self):
        listsquare = [4, 5, 6, 7]
        list2 = map.square_all(listsquare)
        print(list2)
        self.assertEqual(list2, [16, 25, 36, 49])

    # input: self
    # result: assert square of all numbers in a list
    def test_add_n_all(self):
        listadd = [4, 5, 6, 7]
        n = 5
        list2 = map.add_n_all(listadd, n)
        print(list2)
        self.assertEqual(list2, [9, 10, 11, 12])

    # input: self
    # result: assert square of all numbers in a list
    def test_add_n_all_again(self):
        listadd = [1, 2, 3, 4]
        n = 10
        list2 = map.add_n_all(listadd, n)
        print(list2)
        self.assertEqual(list2, [11, 12, 13, 14])

    # input: self
    # result: assert square of all numbers in a list
    def test_distance_all(self):
        listpoint = [point.Point(1, 2), point.Point(3, 4), point.Point(5,5)]
        list5 = map.distance_all(listpoint)
        print(list5)
        self.assertEqual(list5, [2.23606797749979, 5, 7.0710678118654755])

    # input: self
    # result: assert square of all numbers in a list
    def test_distance_all_again(self):
        listpoint = [point.Point(3, 4), point.Point(6, 8), point.Point(8, 15)]
        list5 = map.distance_all(listpoint)
        print(list5)
        self.assertEqual(list5, [5, 10, 17])

    # input: self
    # result: assert  all positive numbers
    def test_are_positive(self):
        listpositive = [1,3,2]
        list6 = map.are_positive(listpositive)
        print(list6)
        self.assertEqual(list6, [1,3,2])

# Run the unit tests.
if __name__ == '__main__':
    unittest.main()

import unittest
from solution import *

class TestAccumulateLeft(unittest.TestCase):
    # tuple tests left
    def test_if_tuple_is_the_collection_given_and_addition_is_the_operation_then_return_correct_result(self):
        self.assertEqual(accumulate_left(lambda a, b: a + b, 64, (2, 4, 8)), 78.0)

    def test_if_tuple_is_the_collection_given_and_subtraction_is_the_operation_then_return_correct_result(self):
        self.assertEqual(accumulate_left(lambda a, b: a - b, 64, (2, 4, 8)), 50.0)

    def test_if_tuple_is_the_collection_given_and_multiplication_is_the_operation_then_return_correct_result(self):
        self.assertEqual(accumulate_left(lambda a, b: a * b, 64, (2, 4, 8)), 4096.0)

    def test_if_tuple_is_the_collection_given_and_division_is_the_operation_then_return_correct_result(self):
        self.assertEqual(accumulate_left(lambda a, b: a / b, 64, (2, 4, 8)), 1.0)

    # list tests left
    def test_if_list_is_the_collection_given_and_addition_is_the_operation_then_return_correct_result(self):
        self.assertEqual(accumulate_left(lambda a, b: a + b, 64, [2, 4, 8]), 78.0)

    def test_if_list_is_the_collection_given_and_subtraction_is_the_operation_then_return_correct_result(self):
        self.assertEqual(accumulate_left(lambda a, b: a - b, 64, [2, 4, 8]), 50.0)

    def test_if_list_is_the_collection_given_and_multiplication_is_the_operation_then_return_correct_result(self):
        self.assertEqual(accumulate_left(lambda a, b: a * b, 64, [2, 4, 8]), 4096.0)

    def test_if_list_is_the_collection_given_and_division_is_the_operation_then_return_correct_result(self):
        self.assertEqual(accumulate_left(lambda a, b: a / b, 64, [2, 4, 8]), 1.0)

class TestAccumulateRight(unittest.TestCase):
    # tuple tests right
    def test_if_tuple_is_the_collection_given_and_addition_is_the_operation_then_return_correct_result(self):
        self.assertEqual(accumulate_right(lambda a, b: a + b, 8, (16, 32, 64)), 120.0)

    def test_if_tuple_is_the_collection_given_and_subtraction_is_the_operation_then_return_correct_result(self):
        self.assertEqual(accumulate_right(lambda a, b: a - b, 8, (16, 32, 64)), 40.0)

    def test_if_tuple_is_the_collection_given_and_multiplication_is_the_operation_then_return_correct_result(self):
        self.assertEqual(accumulate_right(lambda a, b: a * b, 8, (16, 32, 64)), 262144.0)

    def test_if_tuple_is_the_collection_given_and_division_is_the_operation_then_return_correct_result(self):
        self.assertEqual(accumulate_right(lambda a, b: a / b, 8, (16, 32, 64)), 4.0)

    # list tests right
    def test_if_list_is_the_collection_given_and_addition_is_the_operation_then_return_correct_result(self):
        self.assertEqual(accumulate_right(lambda a, b: a + b, 8, [16, 32, 64]), 120.0)

    def test_if_list_is_the_collection_given_and_subtraction_is_the_operation_then_return_correct_result(self):
        self.assertEqual(accumulate_right(lambda a, b: a - b, 8, [16, 32, 64]), 40.0)

    def test_if_list_is_the_collection_given_and_multiplication_is_the_operation_then_return_correct_result(self):
        self.assertEqual(accumulate_right(lambda a, b: a * b, 8, [16, 32, 64]), 262144.0)

    def test_if_list_is_the_collection_given_and_division_is_the_operation_then_return_correct_result(self):
        self.assertEqual(accumulate_right(lambda a, b: a / b, 8, [16, 32, 64]), 4.0)

if __name__ == "__main__":
    unittest.main()
from task1 import group_by_f

from task2 import has_same_ingredients
from task2 import isStronger, leastStronger, strongRelation

from task3 import maxNotes, leading

import unittest


class TestGroupByF(unittest.TestCase):
    def test_function_with_lambda_function(self):
        true_result = group_by_f(lambda a: a % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        expected_result = {False: [1, 3, 5, 7, 9], True: [2, 4, 6, 8, 10]}

        self.assertEqual(true_result, expected_result)

    def test_function_with_standard_len_function(self):
        true_result = group_by_f(len, [[1], [7, 8], [1, 2, 3, 4], [4], ["random", "words"]])
        expected_result = {1: [[1], [4]], 2: [[7, 8], ['random', 'words']], 4: [[1, 2, 3, 4]]}

        self.assertEqual(true_result, expected_result)


class TestHasSameIngredients(unittest.TestCase):
    def test_function_when_result_must_be_true(self):
        medicine1 = ("medicine1", [("p", 5), ("q", 3)])
        medicine2 = ("medicine2", [("p", 4), ("q", 3)])

        self.assertTrue(has_same_ingredients(medicine1, medicine2))

    def test_function_when_result_must_be_true_with_swapped_names(self):
        medicine1 = ("medicine1", [("q", 5), ("p", 3)])
        medicine2 = ("medicine2", [("p", 4), ("q", 3)])

        self.assertTrue(has_same_ingredients(medicine1, medicine2))

    def test_function_when_result_must_be_false(self):
        medicine1 = ("medicine1", [("p", 5)])
        medicine2 = ("medicine2", [("p", 4), ("q", 3)])

        self.assertFalse(has_same_ingredients(medicine1, medicine2))


class TestIsStronger(unittest.TestCase):
    def test_function_when_medicines_are_equal_strength(self):
        medicine1 = ("medicine1", [("p", 5), ("q", 3)])
        medicine2 = ("medicine2", [("p", 4), ("q", 4)])

        self.assertFalse(isStronger(medicine1, medicine2))

    def test_function_when_result_must_be_true(self):
        medicine1 = ("medicine1", [("p", 5), ("q", 3)])
        medicine2 = ("medicine2", [("p", 4), ("q", 3)])

        self.assertTrue(isStronger(medicine1, medicine2))

    def test_function_when_result_must_be_false(self):
        medicine1 = ("medicine1", [("p", 5), ("q", 3)])
        medicine2 = ("medicine2", [("p", 4), ("q", 3)])

        self.assertFalse(isStronger(medicine2, medicine1))


class TestLeastStronger(unittest.TestCase):
    def test_function_when_result_must_be_true(self):
        medicine1 = ("medicine1", [("p", 5), ("q", 3)])
        medicine2 = ("medicine2", [("p", 4), ("q", 3)])
        medicine3 = ("medicine3", [("p", 3)])
        medicine4 = ("medicine4", [("p", 4.5), ("q", 3), ("r", 1)])

        expected_result = ('medicine1', [('p', 5), ('q', 3)])

        self.assertEqual(leastStronger(medicine2, [medicine1, medicine3, medicine4]), expected_result)

    def test_function_when_result_must_be_false(self):
        medicine1 = ("medicine1", [("p", 5), ("q", 3)])
        medicine2 = ("medicine2", [("p", 4), ("q", 3)])
        medicine3 = ("medicine3", [("p", 3)])
        medicine4 = ("medicine4", [("p", 4.5), ("q", 3), ("r", 1)])

        expected_result = []

        self.assertEqual(leastStronger(medicine1, [medicine2, medicine3, medicine4]), expected_result)


class TestStrongRelation(unittest.TestCase):
    def test_function_when_result_must_be_true(self):
        medicine1 = ("medicine1", [("p", 5), ("q", 3)])
        medicine2 = ("medicine2", [("p", 4), ("q", 3)])
        medicine3 = ("medicine3", [("p", 3)])

        expected_result = [(('medicine1', [('p', 5), ('q', 3)]), []), (('medicine2', [('p', 4), ('q', 3)]), ['medicine1']), (('medicine3', [('p', 3)]), ['medicine1', 'medicine2'])]

        self.assertEqual(strongRelation([medicine1, medicine2, medicine3]), expected_result)


class TestMaxNotes(unittest.TestCase):
    def test_function_when_result_must_be_true(self):
        true_result = maxNotes([[1, 2, 3], [2, 2, 2], [9, 7, 3]])
        expected_result = 19

        self.assertEqual(true_result, expected_result)

    def test_function_when_result_must_be_zero(self):
        true_result = maxNotes([])
        expected_result = 0

        self.assertEqual(true_result, expected_result)

    def test_function_when_result_must_be_equal(self):
        true_result = maxNotes([[1, 2, 3], [2, 2, 2]])
        expected_result = 6

        self.assertEqual(true_result, expected_result)


class TestLeading(unittest.TestCase):
    def test_function_when_result_must_be_true(self):
        true_result = leading([[1, 10, 2], [2, 2, 2], [9, 7, 3]])
        expected_result = 2

        self.assertEqual(true_result, expected_result)

    def test_function_when_result_must_be_first_true(self):
        true_result = leading([[1, 2, 3], [2, 2, 2], [9, 7, 3]])
        expected_result = 0

        self.assertEqual(true_result, expected_result)


if __name__ == "__main__":
    unittest.main()

import unittest
from math_quiz import function_A, function_B, function_C


import unittest
from math_quiz import function_A, function_B, function_C


class TestMathGame(unittest.TestCase):

    def test_function_random_integer_between(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = function_random_integer_between(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_random_arithmetic_operator(self):

        # Call the function several times and check if the output is 
        #always one of the valid operators

        for _ in range(1000):  # Test a large number of random values
            operator = function_random_arithmetic_operator()
            self.assertIn(operator, ['+', '-', '*'])

    def test_function_Calculate(self):
        #test cases to be checked
        test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (8, 3, '-', '8 - 3', 5),
                (4, 6, '*', '4 * 6', 24),
                (10, 5, '+', '10 + 5', 15),
                (12, 4, '-', '12 - 4', 8),
                (3, 7, '*', '3 * 7', 21),
                (9, 2, '+', '9 + 2', 11),
                (15, 6, '-', '15 - 6', 9),
                (2, 8, '*', '2 * 8', 16),
            ]
        #Call the function for the number of test cases and compare 
        #the calculated expression and answer to the test cases
        for num1, num2, operator, expected_problem, expected_answer in test_cases:

            problem, answer = function_Calculate(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
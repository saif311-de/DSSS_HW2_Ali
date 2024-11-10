import random

def function_random_integer_between(min, max):
    """
    Generate a random integer between the given min and max values.

    Parameters
    ----------
    min : integer
      minimum value
    max : integer
      maximum value

    Returns
    -------
    integer
      random integer between the min and max value
    """
    if not isinstance(min, int) or not isinstance(max, int):    # Checks if the input values are integers.
        raise ValueError("min and max must be integers.")         

    return random.randint(min, max)                             # Returns a random value between the given args


def function_random_arithmetic_operator():
    """
    Generates a random arithmetic operator.

    Returns
    -------
    str
      A string representing a random arithmetic operator: '+', '-', or '*'.
    """
    return random.choice(['+', '-', '*'])


def function_Calculate(num1, num2, operator):
    """
    Perform a basic arithmetic operation (addition, subtraction, or multiplication) 
    between two integers based on the specified operator.

    Parameters
    ----------
    num1 : int
        The first integer in the operation.
    num2 : int
        The second integer in the operation.
    operator : str
        The arithmetic operator, which can be '+' for addition, '-' for subtraction,
        or '*' for multiplication.

    Returns
    -------
    tuple
        A tuple containing:
        - expression (str): A string representing the operation in the format "num1 operator num2".
        - result (int): The result of the arithmetic operation.
    """
    expression = f"{num1} {operator} {num2}"    # Create a string representation of the operation
    
    # Perform the calculation based on the specified operator
    if operator == '+':
        result = num1 + num2  					# Add num1 and num2 if the operator is '+'
    elif operator == '-':
        result = num1 - num2  					# Subtract num2 from num1 if the operator is '-'
    else:
        result = num1 * num2  					# Multiply num1 and num2 if the operator is anything else
    
    # Return both the expression string and the result of the operation
    return expression, result


def math_quiz():
    score = 0
    total_questions = 3  # Set to a fixed number for testing

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        # Generate random numbers and operator
        num1 = function_random_integer_between(1, 10)
        num2 = function_random_integer_between(1, 10)
        operator = function_random_arithmetic_operator()

        # Create the problem and calculate the answer
        problem, answer = function_Calculate(num1, num2, operator)
        print(f"\nQuestion: {problem}")
        
        try:
            # Get user's answer and check if it's correct
            user_answer = int(input("Your answer: "))
            
            if user_answer == answer:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {answer}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()
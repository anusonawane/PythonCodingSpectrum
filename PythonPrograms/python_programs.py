# Coding spectrum is a type of class where u can do basic coding challenges by calling single class
# Author: Anushka Sonawane and Chinmay Bhalerao

class PythonPrograms:
    def __init__(self):
        pass

    # To return hello world
    def hello_world():
        return 'hello world'

    # To sum two numbers
    def sum(a, b):
        """
        This function returns the sum of two numbers
        Args:
            a: int or float, first number
            b: int or float, second number

        Returns:
                int or float, sum of two numbers
        """
        return a + b

    # To find largest number
    def largest(a, b):
        """
        This function finds the largest number
        Args:
            a:int or float , First number
            b:int or float , Second number

        Returns:
            Sum of two numbers

        """
        if a == b:
            return f"Enter two different numbers"
        if a < b:
            return f"The Largest number is {a}"
        else:
            return f"The largest number is {b}"

    # Function to check if two the number is even or odd
    def even_or_odd(number):
        """
        Check if  number is even or odd

        Args:
            number: int, number to check

        Returns:
            number even or odd result
        """
        if number == 0 or number == 1 or number == 2:
            return f"enter a valid number"
        if number % 2 == 0:
            return f"Given number is EVEN"
        else:
            return f"Given number is ODD"

    # Simple calculator
    # Assuming calculation is of only 2 numbers
    def calculate(num1, num2):
        """
        Acts as a Simple calculator
        Args:
            num1: int or float, number
            num2: int or float, number

        Returns:
            Required operation's result


        """
        IP = input("what operation you want to do? Press[Addition, Substaction ,Multiplication ,Division] ")
        if IP == "Addition":
            return f"Addition is {num1+num2}"
        if IP == "Substaction":
            return f"Substaction is {num1 - num2}"
        if IP == "Multiplication":
            return f"Multiplication is {num1*num2}"
        if IP == "Division":
            return f"Division is {num1/num2}"
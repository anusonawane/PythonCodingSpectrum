# Coding spectrum is a type of class where you can do basic coding challenges by calling single class
# Author: Anushka Sonawane and Chinmay Bhalerao

class PythonPrograms:
    def __init__(self):
        pass

    # Level 1
    # ----------------------------------------------------------------#

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
        IP = input("what operation you want to do? Press[Addition, Substaction , Multiplication ,Division] ")
        if IP == "Addition":
            return f"Addition is {num1+num2}"
        if IP == "Substaction":
            return f"Substaction is {num1 - num2}"
        if IP == "Multiplication":
            return f"Multiplication is {num1*num2}"
        if IP == "Division":
            return f"Division is {num1/num2}"

    # Level 2
    # ----------------------------------------------------------------#
    # Factorial of the number
    def fact(number):
        """
        This is brute force code to find factorial of a number

        Args:
            number:int, number for which you have to find factorial

        Returns:
            fact::int, Factorial of given number
        """
        fact = 1
        if number == 0:
            return "Enter valid number"
        for i in range(1, number+1):
            fact = fact*i
        return fact

    # Prime number
    def prime_or_not(num):
        """
        This function will give you idea about the Prime numbers

        Args:
            num (int) : The number which we want to see Prime or not

        Returns:
            string : Telling prime or not

        """
        if num == 1:
            return "1 is neither prime nor composite."
        else:
            for i in range(2, int(num**0.5) + 1):
                # Checking only upto square root numbers to reduce complexity
                if num % i != 0 and num % num == 0 and num % 1 == 0:
                    return "The given number is a PRIME number"
                else:
                    return "The given number is NOT A PRIME number"

    # Function to calculate fibonacci series
    def fibonacci_series(num):
        """
        This function takes number and returns
          fibonacci series upto that number

        Args:
            num (int): number upto which we want to calculate fibonacci series

        Returns:
            Series (list): fibonacci series

        """

        i = 0
        a = 0
        b = 1
        series = []
        while i < num+1:
            series.append(a)
            c = a+b
            a = b
            b = c
            i += 1
        return series

    def get_reversed_string(word):
        """
        This function will reverse the string

        Args:
            word (str): The string to reverse

        Returns:
            reversed string (str): The string
        """
        for i in word[::-1]:
            print(i)

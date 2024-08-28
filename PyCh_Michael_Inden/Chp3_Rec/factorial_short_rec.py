# one line code to get factorial of a number recursively

"""
python short cut: the calculation can be compressed to one line or function
can be compressed to one line using or in the form of a lambda as a one liner. 

Lambdas usually encapsulate only a tiny piece of functionality and thus you should not name them and assign them to a variable.
"""
factorial = lambda n: n if n ==1 else n * factorial(n -1)

if __name__ == "__main__":
    val_1 = factorial(5)
    print("The factorial of a given number is ", val_1)
"""
Calculation of the sum in python:
you can convert the recursive calculation formula of the summation intoa recursive function.

"""
def sum_of(n):
    if n <= 0:
        raise ValueError("n must be >= 1")
    
    # recursive termination

    if n == 1:
        return 1
    
    # recursive descent

    return n + sum_of(n-1)

if __name__ == "__main__":
    sum_of_n = sum_of(5)
    print("Yay, recursive function to calculate sum of n is", sum_of_n)
def factorial(n):
    if n < 0:
        raise ValueError("n must be >=0")
    # recursion termination
    if n == 0 or n == 1:
        return 1
    
    # recursive descent

    return n * factorial(n-1)

if __name__ == "__main__":
    val = factorial(5)
    print("Yay, recursive value of 5 is ", val)

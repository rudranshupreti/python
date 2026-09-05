# Given a number n, check whether it is even or odd. Return true for even and false for odd.
def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    n = 15
    if isEven(n):
        print("true")
    else:
        print("false")

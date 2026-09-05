# Given a number n, we need to print its table.
def table(n):
    for i in range(1, 11):
        # print("%d * %d = %d" % (n, i, i * n))
        print(f"{n} * {i} = {n*i}")


if __name__ == "__main__":
    n = 4
    table(n)

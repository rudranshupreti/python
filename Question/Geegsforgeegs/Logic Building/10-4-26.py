# Given two integers n and m (m != 0). Find the number closest to n and divisible by m. If there is more than one such number, then output the one having maximum absolute value.
def close_num(n, m):
    remind = n % m

    lower = n - remind
    upper = n - (remind - m)

    if remind < m / 2:
        return lower
    elif remind < m / 2:
        return upper
    else:
        return max(upper, lower)


print(close_num(162, 4))

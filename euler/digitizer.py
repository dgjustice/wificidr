num = 2**1000

print(num)
def int_to_digits(num):
    digits = []
    i = 1
    while num >= 10**(i - 1):
        digit = (num % (10**i) - (num % (10**(i - 1)))) // (10**(i - 1))
        i += 1
        digits.append(digit)
    return reversed(digits)

# Project Euler 16, not cheating with strings
print(sum(list(int_to_digits(num))))

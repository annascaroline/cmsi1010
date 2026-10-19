def blocks(n):
    return 0 if n <= 0 else blocks(n-1) + n


print(blocks(8))
print(blocks(0))
print(blocks(-1))
print(blocks(1))
# print(blocks(838852)) --> python had to run loop 1000+ times so it gave error
print(blocks(998))

# challenges

# factorial


def factorial(n):
    return 1 if n == 0 else n*factorial(n-1)

# sum of digits n
# base case = n < 10, recursive step = n // 10 + n % 10


def sum_of_digits(n):
    return n if n < 10 else sum_of_digits(n//10) + (n % 10)

# is_palindrome
# base case = len(s) <= 1, recursive step = s==s[::-1]


def is_palindrome(s):
    return len(s) <= 1 or (s == s and is_palindrome(s[::-1]))

# USING FOR LOOP - iterative solution
"""
def print_count_down(n):
    for count in range(n, 0, -1):
        print(count)
    print("BOOM")
"""
# USING RECURSION
def print_count_down(n):
    if n <= 0:
        print("BOOM")
    else:
        print(n)
        print_count_down(n-1)

print_count_down(-2)


#Write a recursive function that calculates the sum of all digits in a positive integer.
def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_of_digits(n // 10)
# Test your code:
print(sum_of_digits(123)) # Should print: 6
print(sum_of_digits(4567)) # Should print: 22
print(sum_of_digits(5)) # Should print: 5
print(sum_of_digits(0)) # Should print: 0
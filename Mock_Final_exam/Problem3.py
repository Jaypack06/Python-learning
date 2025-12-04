#Write a function that safely divides two numbers and handles all possible errors.
def safe_divide(a, b):
    """
    Safely divide two numbers with error handling.
    Args:
    a: numerator (string or number)
    b: denominator (string or number)
    Returns:
    Result of a/b if successful
    "Error: Cannot divide by zero" if b is 0
    "Error: Invalid input" if inputs can't be converted to numbers
    Examples:
    safe_divide(10, 2) → 5.0
    safe_divide("10", "2") → 5.0
    safe_divide(10, 0) → "Error: Cannot divide by zero"
    safe_divide("abc", 2) → "Error: Invalid input"
    """
    try:
        num = float(a)
        denom = float(b)
        if denom == 0:
            return "Error: Cannot divide by zero"
        return num / denom
    except ValueError:
        return "Error: Invalid input"
# YOUR CODE HERE
# Hint: You'll need try-except blocks
# Hint: Convert inputs to float first
# Hint: Check for division by zero
# Test your code:
print(safe_divide(10, 2)) # 5.0
print(safe_divide("10", "2")) # 5.0
print(safe_divide(10, 0)) # Error: Cannot divide by zero
print(safe_divide("abc", 2)) # Error: Invalid input
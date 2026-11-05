# Recursive function to return the n-th Fibonacci number
def fibonacci_recursive(n):
    # Base cases: return 0 for the 1st term, 1 for the 2nd term
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case: add the two preceding terms
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Define how many terms you want to print
number_of_terms = 10

print(f"Fibonacci sequence up to {number_of_terms} terms:")
for i in range(number_of_terms):
    print(fibonacci_recursive(i), end=" ")

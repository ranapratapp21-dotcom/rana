# 1. Take user input
num = int(input("Enter a positive integer: "))

# 2. Store the original number in a temporary variable for calculation
temp = num

# 3. Find the number of individual digits (order n) using a loop
order = 0
while temp > 0:
    order += 1
    temp //= 10

# 4. Reset temp to calculate the sum of digits raised to the power of n
temp = num
digit_sum = 0

# 5. Extract each digit, raise it to the power of n, and sum them up using a loop
while temp > 0:
    digit = temp % 10            # Extract the last digit
    
    # Calculate digit^order using a loop (instead of ** operator)
    power_result = 1
    for _ in range(order):
        power_result *= digit
        
    digit_sum += power_result    # Add to the total sum
    temp //= 10                  # Remove the last digit

# 6. Check whether the number is Armstrong or not using a conditional statement
if num == digit_sum:
    print(f"{num} is an Armstrong Number.")
else:
    print(f"{num} is NOT an Armstrong Number.")

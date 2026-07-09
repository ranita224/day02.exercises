# Ask the user for their age
age_text = input("Enter your age: ")

# Convert the input (string) to an integer
age = int(age_text)

# Calculate what their age will be next year
next_year = age + 1

# Display the result
print("Next year, you will be", next_year, "years45 old.")
print(2 + 2)
# Arithmetic operators in action

a = 10
b = 3


# Addition, subtraction, multiplication
print("Addition:", a + b)        # 13
print("Subtraction:", a - b)     # 7
print("Multiplication:", a * b)  # 30

# Division (always gives a float)
print("Division:", a / b)        # 3.333...

# Floor division (drops remainder)
print("Floor Division:", a // b) # 3

# Modulo (remainder)
print("Modulo:", a % b)          # 1

# Exponent (power)
print("Exponent:", a ** b)       # 1000
# Comparison and logical operators in action

balance = 1500
is_member = True

# Comparison operators
print(balance == 1500)      # True
print(balance != 1000)      # True
print(balance > 1000)       # True
print(balance < 2000)       # True

# Logical operators
print(balance > 1000 and is_member)  # True (both conditions are True)
print(balance < 1000 or is_member)   # True (one condition is True)
print(not is_member)                 # False (negates True)

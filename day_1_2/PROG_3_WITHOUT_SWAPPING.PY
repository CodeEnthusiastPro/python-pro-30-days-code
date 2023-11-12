# Get input from the user or assign values to variables
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

# Print the values before swapping
print("Before swapping: a =", a, "b =", b)

# Swap the values without using a third variable
a = a + b
b = a - b
a = a - b

# Print the values after swapping
print("After swapping: a =", a, "b =", b)

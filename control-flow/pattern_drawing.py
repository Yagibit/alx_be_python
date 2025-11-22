# pattern_drawing.py

# Ask the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to handle rows
while row < size:
    # Use a for loop to print asterisks in each row
    for i in range(size):
        print("*", end="")

    # Move to the next line after each row
    print()

    # Increment the row counter
    row += 1

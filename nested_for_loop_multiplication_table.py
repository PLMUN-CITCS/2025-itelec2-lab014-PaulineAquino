# Outer loop for rows (1 to 5)
for i in range(1, 6):
    # Inner loop for columns (1 to 5)
    for j in range(1, 6):
        # Calculate the product of i and j
        product = i * j
        # Print the product with formatting, ensuring consistent spacing
        print(f"{product:4}", end="")  
    # Move to the next line after each row
    print()

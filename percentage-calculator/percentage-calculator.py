def get_float_input(prompt, allow_zero=False):
    """
    Prompts the user for a float input until a valid number is entered.
    
    Args:
        prompt (str): The message to display to the user.
        allow_zero (bool): Whether to allow zero as a valid input.
    
    Returns:
        float: The valid float input from the user.
    """
    while True:
        try:
            value = float(input(prompt))  # Attempt to convert input to float
            if not allow_zero and value <= 0:
                print("Error: Value must be greater than zero.")  # Error message for non-positive input
                continue
            return value  # Return the valid float value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")  # Error message for invalid input

# Get user input for current and target amounts with error checking
current_amount = get_float_input("Please enter the current amount (e.g., 1.5): ")
target_amount = get_float_input("Please enter the target amount (must be greater than zero): ", allow_zero=False)

# Calculate the percentage of the current amount relative to the target amount
percentage = (current_amount / target_amount) * 100
# Calculate the remaining amount needed to reach the target
subtraction = target_amount - current_amount

# Store the current and target amounts for output
curr = current_amount  # Keep as float for accurate representation
tar = target_amount    # Keep as float for accurate representation
sub = subtraction      # Keep as float for accurate representation

# Format current amount based on its value
if curr.is_integer():
    current = str(int(curr))  # Convert to int if it's a whole number
else:
    current = f"{curr:.2f}"    # Format to 2 decimal places if not

target = int(tar)              # Convert target to integer for display
percent = str(percentage)       # Convert percentage to string to preserve all decimal places
minus = f"{sub:.2f}"           # Format remaining amount to 2 decimal places

# Decision and output messages
if current_amount < target_amount:
    print(f"\nThe current amount of {current} is {percent}% of the target amount of {target}.")
    print(f"You need an additional {minus} to reach your target of {target}.")
elif current_amount == target_amount:
    print("\nCongratulations! You have reached 100% of your target amount.")
else:
    print(f"\nThe current amount ({current}) exceeds the target amount ({target}).")

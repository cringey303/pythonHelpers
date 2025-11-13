from validinput import ValidInput

# --- Get a valid integer ---
# This will loop until a valid integer is entered.
age = ValidInput.get_int_input("Enter your age: ")

# --- Get a valid integer in a range ---
# This will loop until an integer between 1 and 5 is entered.
rating = ValidInput.get_int_input("Enter a rating (1-5): ", min=1, max=5)
print(f"You rated: {rating}")


# --- Get a valid float ---
# This will loop until a valid float is entered.
price = ValidInput.get_float_input("Enter a price: ")

# --- Get a valid float in a range ---
# This will loop until a float between 1.00 and 99.99 is entered.
price = ValidInput.get_float_input("Enter price ($1.00 - $99.99): ", min=1.0, max=99.99)
print(f"Price set: ${price:.2f}")


# --- Get a valid file name ---
# This will loop until the user enters a valid-looking .txt filename
# that also exists in the same directory.
filename = ValidInput.get_valid_file_name('txt')
print(f"Accessing file: {filename}")


# --- Get a list of integers ---
# The user must enter a comma-separated list, e.g., "1, 2, 3"
scores = ValidInput.get_int_list_input("Enter scores (0-100), separated by commas: ", min=0, max=100)
print(f"Your scores: {scores}")
# pythonHelpers

Some Python helper modules for terminal colors, validated user input, and custom errors.

## How to Use

To use these helpers, place the `.py` files (`colors.py`, `errors.py`, `validinput.py`) in your project's directory, then import the classes and functions directly into your scripts.

---

## `colors.py`

Provides a `Colors` class for adding ANSI colors to terminal output.

**Note:** The `color_item` method as written does not work as a class or static method. The best way to use this class is by accessing its color attributes.

### Example Usage

```python
from colors import Colors as c

# Use f-strings to add color to your text
print(f"{c.GREEN}Success!{c.RESET} The file was saved.")
print(f"{c.RED}Error:{c.RESET} File not found.")
print(f"{c.YELLOW}Warning:{c.RESET} Please check your input.")
print(f"{c.BLUE}This is blue text.{c.RESET}")
print(f"{c.PURPLE}This is purple text.{c.RESET}")
print(f"{c.CYAN}This is cyan text.{c.RESET}")
```
Output:

<img width="410" height="153" alt="Screenshot 2025-11-13 at 11 38 35" src="https://github.com/user-attachments/assets/ad236098-6854-4e3c-be70-7a26570bc400" />


## `errors.py`

Provides custom exceptions ParserError and StateException.

### Example Usage
Use try-except blocks when implementing:
```python
from errors import ParserError, StateException
from colors import Colors as c # For colored error messages

def parse_my_data(data):
    """A function that could fail with a custom error."""
    if data == "bad":
        raise ParserError("Invalid format.")
    if data == "stuck":
        raise StateException("The machine is in an unrecoverable state.")
    return f"Parsed data: {data}"

# --- ParserError Example ---
try:
    print(parse_my_data("good"))
    print(parse_my_data("bad"))
except ParserError as e:
    print(f"{c.RED}Parser error: {e.message}{c.RESET}")
except StateException as e:
    print(f"{c.YELLOW}State exception: {e.message}{c.RESET}")

# --- StateException Example ---
try:
    print(parse_my_data("stuck"))
except ParserError as e:
    print(f"{c.RED}Parser error: {e.message}{c.RESET}")
except StateException as e:
    print(f"{c.YELLOW}State exception: {e.message}{c.RESET}")
```
Output:

<img width="616" height="94" alt="Screenshot 2025-11-13 at 11 48 01" src="https://github.com/user-attachments/assets/81a8a8c5-6265-4a9b-a145-8d4337a38dbd" />

## `validinput.py`

Provides static methods to get valid user input, continuously looping until exit or valid input.

### Example Usage
```python
from validinput import ValidInput

# --- Get valid integer ---
# Loop until a valid integer is entered.
age = ValidInput.get_int_input("Enter your age: ")

# --- Get valid integer in a range ---
# Loop until an integer between 1 and 5 is entered.
rating = ValidInput.get_int_input("Enter a rating (1-5): ", min=1, max=5)
print(f"You rated: {rating}")


# --- Get valid float ---
# Loop until a valid float is entered.
price = ValidInput.get_float_input("Enter a price: ")

# --- Get valid float in a range ---
# Loop until a float between 1.00 and 99.99 is entered.
price = ValidInput.get_float_input("Enter price ($1.00 - $99.99): ", min=1.0, max=99.99)
print(f"Price set: ${price:.2f}")


# --- Get valid file name ---
# Loop until the user enters a valid .txt filename
# that exists in the same directory.
# Can change 'extension' argument to any file extension (e.g. csv, tsv, txt)
filename = ValidInput.get_valid_file_name('txt')
print(f"Accessing file: {filename}")


# --- Get a list of integers ---
# Get a comma-separated list of ints, e.g., "1, 2, 3"
scores = ValidInput.get_int_list_input("Enter scores (0-100), separated by commas: ", min=0, max=100)
print(f"Your scores: {scores}")
```
Output:

<img width="563" height="377" alt="Screenshot 2025-11-13 at 14 26 59" src="https://github.com/user-attachments/assets/f8ba5b3c-cfb2-4aa0-bd7b-744da7e8c520" />

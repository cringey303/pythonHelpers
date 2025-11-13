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

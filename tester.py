# Use this file to test these helpers for yourself

import os
from colors import Colors as c
from errors import ParserError, StateException
from validinput import ValidInput

def test_colors():
    """Demonstrates all available colors."""
    print(f"\n{c.WHITE}=== 1. Testing Colors ==={c.RESET}")
    print(f"{c.RED}This is RED{c.RESET}")
    print(f"{c.GREEN}This is GREEN{c.RESET}")
    print(f"{c.YELLOW}This is YELLOW{c.RESET}")
    print(f"{c.BLUE}This is BLUE{c.RESET}")
    print(f"{c.PURPLE}This is PURPLE{c.RESET}")
    print(f"{c.CYAN}This is CYAN{c.RESET}")
    print(f"{c.GREY}This is GREY{c.RESET}")
    print(f"{c.WHITE}This is WHITE{c.RESET}")

def test_errors():
    """Demonstrates catching custom errors."""
    print(f"\n{c.WHITE}=== 2. Testing Custom Errors ==={c.RESET}")
    
    def risky_function(action):
        if action == "parse":
            raise ParserError("Failed to parse the data string.")
        elif action == "state":
            raise StateException("System entered an invalid state.")
        else:
            return "Success!"

    # Test ParserError
    try:
        print("Attempting parse...")
        risky_function("parse")
    except ParserError as e:
        print(f"{c.RED}Caught Expected ParserError: {e.message}{c.RESET}")

    # Test StateException
    try:
        print("Checking state...")
        risky_function("state")
    except StateException as e:
        print(f"{c.YELLOW}Caught Expected StateException: {e.message}{c.RESET}")

def test_inputs():
    """Demonstrates valid input helpers."""
    print(f"\n{c.WHITE}=== 3. Testing Valid Inputs ==={c.RESET}")
    
    # 1. Integer Test
    print(f"\n{c.CYAN}Test: get_int_input (No Range){c.RESET}")
    age = ValidInput.get_int_input("Enter an integer (e.g. age): ")
    print(f"{c.GREEN}Accepted: {age}{c.RESET}")

    # 2. Integer Range Test
    print(f"\n{c.CYAN}Test: get_int_input (Range 1-5){c.RESET}")
    rating = ValidInput.get_int_input("Enter a rating (1-5): ", min=1, max=5)
    print(f"{c.GREEN}Accepted: {rating}{c.RESET}")

    # 3. Float Test
    print(f"\n{c.CYAN}Test: get_float_input (Range 0.0 - 1.0){c.RESET}")
    prob = ValidInput.get_float_input("Enter a probability (0.0-1.0): ", min=0.0, max=1.0)
    print(f"{c.GREEN}Accepted: {prob}{c.RESET}")

    # 4. File Test
    print(f"\n{c.CYAN}Test: get_valid_file_name ('txt'){c.RESET}")
    # Create a dummy file so the user has something to type that works
    dummy_filename = "test.txt"
    with open(dummy_filename, "w") as f:
        f.write("This is a temporary file for testing.")
    print(f"{c.GREY}(Created temporary file '{dummy_filename}' for testing){c.RESET}")
    
    try:
        filename = ValidInput.get_valid_file_name("txt")
        print(f"{c.GREEN}Accepted: {filename}{c.RESET}")
    finally:
        # Clean up the dummy file
        if os.path.exists(dummy_filename):
            os.remove(dummy_filename)
            print(f"{c.GREY}(Removed temporary file '{dummy_filename}'){c.RESET}")

    # 5. Integer List Test
    print(f"\n{c.CYAN}Test: get_int_list_input{c.RESET}")
    scores = ValidInput.get_int_list_input("Enter scores (0-100) separated by commas: ", min=0, max=100)
    print(f"{c.GREEN}Accepted list: {scores}{c.RESET}")

if __name__ == "__main__":
    try:
        test_colors()
        test_errors()
        test_inputs()
        print(f"\n{c.GREEN}=== Tests Completed ==={c.RESET}")
    except KeyboardInterrupt:
        print(f"\n{c.RED}Test Aborted.{c.RESET}")
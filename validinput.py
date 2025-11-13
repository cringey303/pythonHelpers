from colors import Colors as c

class ValidInput:
    def get_int_input(prompt, min=None, max=None) -> int:
        while True:
            try:
                value = int(input(prompt))
                if min is not None and max is not None and not (min <= value <= max):
                    print(f'{c.RED}Invalid input. Enter a number from {min}-{max} (inclusive).{c.RESET}')
                else:
                    return value
            except ValueError:
                print(f'{c.RED}Invalid input. Please enter an integer.{c.RESET}')
                
    def get_float_input(prompt, min=None, max=None) -> float:
        while True:
            try:
                value = float(input(prompt))
                if min is not None and max is not None and not (min <= value <= max):
                    print(f'{c.RED}Invalid input. Enter a number from {min}-{max} (inclusive).{c.RESET}')
                else:
                    return value
            except ValueError:
                print(f'{c.RED}Invalid input. Please enter a float.{c.RESET}')
                
    def get_valid_file_name(extension) -> str:
        while True:
            file = input('Enter the name of the input file: ')
            if file.startswith(' ') or file.startswith('.') or file.startswith('-') or file.startswith('_') or '\\' in file or '/' in file or ':' in file or '*' in file or '?' in file or '"' in file or '<' in file or '>' in file or '|' in file or ':' in file:
                print(f'{c.RED}Invalid input. Please enter a valid file name.{c.RESET}')
            elif file.endswith('.' + extension):
                file+=''
            elif "." in file and not file.endswith(f'.{extension}'):
                print(f"{c.RED}Invalid file type. Please enter a .{extension} file{c.RESET}")
            else:
                file += f'.{extension}'
            try:
                with open(file, 'r') as f:
                    print(f"File found: {c.GREEN}{file}{c.RESET}")
                    return file
            except FileNotFoundError:
                print(f"{c.RED}File not found. Please enter a valid file name.{c.RESET}")
                
    def get_int_list_input(prompt, min=None, max=None) -> list:
        while True:
            try:
                value = input(prompt)
                ls = [int(i) for i in value.split(',')]
                if min is not None and max is not None and not all(min <= i <= max for i in ls):
                    print(f'{c.RED}Invalid input. Enter numbers from {min}-{max} (inclusive).{c.RESET}')
                else:
                    return ls
            except ValueError:
                print(f'{c.RED}Invalid input. Please enter a list of integers.{c.RESET}')
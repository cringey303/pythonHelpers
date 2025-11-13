class Colors:
    def __init__(self):
        pass
    
    RESET = "\033[0m"

    # Colors \033[1;
    GREY = "\033[1;30m"
    RED = "\033[1;31m"
    GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    BLUE = "\033[1;34m"
    PURPLE = "\033[1;35m"
    CYAN = "\033[1;36m"
    WHITE = "\033[1;37m"
    
    def color_item(item: str, color: str):
        return f"{getattr(Colors,color)}{item}{Colors.RESET}"
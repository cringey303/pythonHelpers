from colors import Colors as c

class ParserError(Exception):
    def __init__(self, message: str):
        self.message = message
        
        
class StateException(Exception):
    def __init__(self, message: str):
        self.message = message
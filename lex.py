class Lexer:
    def __init__(self, source):
        pass

    # Process the next character
    def nextChar(self):
        pass

    # Return the lookhead of the character
    def peek(self):
        pass

    # Invalid token found, print error message and exit
    def abort(self, message):
        pass

    # Skip whitespace except new lines, this marks end of statement
    def skipWhitespace(self):
        pass

    # Ignore comments in code
    def comments(self):
        pass

    # Return next token
    def getToken(self):
        pass

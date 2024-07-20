class Lexer:
    def __init__(self, source):
        self.source = source + '\n'
        # source code to lex as a string. Append a new line to simplify lexing
        self.curChar = ''
        # current character in the string
        self.curPos = -1
        # current position in the string
        self.nextChar()
        pass

    # Process the next character
    def nextChar(self):
        self.curPos += 1
        if self.curPos >= len(self.source):
            self.curChar = '\0'
        else:
            self.curChar = self.source[self.curPos]
        pass

    # Return the lookhead of the character
    def peek(self):
        if self.curPos + 1 >= len(self.source):
            return '\0'
        return self.source[self.curPos+1]
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

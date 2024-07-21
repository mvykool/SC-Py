import enum


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
        # Check the first character of this token to see
        # if we can decide what it is.
        # If it is a multiple character operator
        # (e.g., !=), number, identifier, or keyword
        # then we will process the rest.
        if self.curChar == '+':
            pass  # plus
        elif self.curChar == '-':
            pass  # minus
        elif self.curChar == '*':
            pass  # multiply
        elif self.curChar == '/':
            pass  # slash
        elif self.curChar == '\n':
            pass  # new line
        elif self.curChar == '\0':
            pass  # EOF
        else:
            # unknown token
            pass

        self.nextChar()
        pass

# Token contains original text and kind of tokensh


class Token:
    def __init__(self, tokenText, tokenKind):
        self.text == tokenText
        #  text used for identifiers, strings and numbers
        self.kind == tokenKind
        #  type the token is classified as

#  TokenType is our enum for all our types of tokens


class TokenType(enum.Enum):
    EOF = -1
    NEWLINE = 0
    NUMBER = 1
    IDENT = 2
    STRING = 3
    # KEYWORDS
    LABEL = 101
    GOTO = 102
    PRINT = 103
    INPUT = 104
    LET = 105
    IF = 106
    THEN = 107
    ENDIF = 108
    WHILE = 109
    REPEAT = 110
    ENDWHILE = 111
    #  OPERATORS
    EQ = 201
    PLUS = 202
    MINUS = 203
    ASTERISK = 204
    SLASH = 205
    EQEQ = 206
    NOTEQ = 207
    LT = 208
    LTEQ = 209
    GT = 110
    GTEQ = 111

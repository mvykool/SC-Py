import enum
import sys


class Lexer:
    def __init__(self, source):
        self.source = source + '\n'
        # source code to lex as a string. Append a new line to simplify lexing
        self.curChar = ''
        # current character in the string
        self.curPos = -1
        # current position in the string
        self.nextChar()

    # Process the next character
    def nextChar(self):
        self.curPos += 1
        if self.curPos >= len(self.source):
            self.curChar = '\0'
        else:
            self.curChar = self.source[self.curPos]

    # Return the lookhead of the character
    def peek(self):
        if self.curPos + 1 >= len(self.source):
            return '\0'
        return self.source[self.curPos+1]

    # Invalid token found, print error message and exit
    def abort(self, message):
        sys.exit("Lexing error " + message)

    # Skip whitespace except new lines, this marks end of statement
    def skipWhitespace(self):
        while self.curChar == ' ' or self.curChar == '\t' or self.curChar == '\r':
            self.nextChar()

    # Ignore comments in code
    def comments(self):
        if self.curChar == '~':
            while self.curChar != '\n':
                self.nextChar()

    # Return next token

    def getToken(self):
        self.skipWhitespace()
        self.comments()
        token = None

        # Check the first character of this token to see
        # if we can decide what it is.
        # If it is a multiple character operator
        # (e.g., !=), number, identifier, or keyword
        # then we will process the rest.
        if self.curChar == '+':
            token = Token(self.curChar, TokenType.PLUS)
        elif self.curChar == '-':
            token = Token(self.curChar, TokenType.MINUS)
        elif self.curChar == '*':
            token = Token(self.curChar, TokenType.ASTERISK)
        elif self.curChar == '/':
            token = Token(self.curChar, TokenType.SLASH)

        elif self.curChar == '=':
            #  check if this is only = or  ==
            if self.peek() == '=':
                lastChar = self.curChar
                self.nextChar()
                token = Token(lastChar + self.curChar, TokenType.EQEQ)
            else:
                token = Token(self.curChar, TokenType.EQ)

        elif self.curChar == '>':
            #  check if this is only > or  >=
            if self.peek() == '=':
                lastChar = self.curChar
                self.nextChar()
                token = Token(lastChar + self.curChar, TokenType.GTEQ)
            else:
                token = Token(self.curChar, TokenType.GT)

        elif self.curChar == '<':
            #  check if this is only < or  <=
            if self.peek() == '=':
                lastChar = self.curChar
                self.nextChar()
                token = Token(lastChar + self.curChar, TokenType.LTEQ)
            else:
                token = Token(self.curChar, TokenType.LT)

        elif self.curChar == '!':
            if self.peek() == '=':
                lastChar = self.curChar
                self.nextChar()
                token = Token(lastChar + self.curChar, TokenType.NOTEQ)
            else:
                self.abort("Expected !=, got !" + self.peek())

        elif self.curChar == '\"':
            #  get characters between quotations
            self.nextChar()
            startPos = self.curPos

            while self.curChar != '\"':
                #  no allow special characters in strings
                #  no scape characters, newlines, tabs
                #  we'll be using C printf on this string
                if self.curChar == '\r' or self.curChar == '\n' or self.curChar == '\t' or self.curChar == '\\' or self.curChar == '%':
                    self.abort("Illegal characters in string")
                self.nextChar()

            tokText = self.source[startPos: self.curPos]  # get substring
            token = Token(tokText, TokenType.STRING)

        elif self.curChar.isdigit():
            #  leading character is a digit, so its a number
            #  get all all characters and decimal if exist
            startPos = self.curPos
            while self.peek().isdigit():
                self.nextChar()
            if self.peek() == '.':  # decimal
                self.nextChar()

                #  must have at least one digit after decimal
                if not self.peek().isdigit():
                    #  Error
                    self.abort("Illegal character in number")
                while self.peek().isdigit():
                    self.nextChar()

            tokText = self.source[startPos: self.curPos + 1]  # get substring
            token = Token(tokText, TokenType.NUMBER)

        elif self.curChar.isalpha():
            # Leading character is a letter, so this must be an identifier or a keyword.
            # Get all consecutive alpha numeric characters
            startPos = self.curPos
            while self.peek().isalnum():
                self.nextChar()

            #  check if the token is in the list of KEYWORDS
            tokText = self.source[startPos: self.curPos + 1]  # get substring
            keyword = Token.checkIfKeyword(tokText)
            if keyword == None:
                token = Token(tokText, TokenType.IDENT)
            else:
                token = Token(tokText, keyword)

        elif self.curChar == '\n':
            token = Token(self.curChar, TokenType.NEWLINE)
        elif self.curChar == '\0':
            token = Token(self.curChar, TokenType.EOF)
        else:
            # unknown token
            self.abort("Unknown token: " + self.curChar)

        self.nextChar()
        return token

# Token contains original text and kind of tokensh


class Token:
    def __init__(self, tokenText, tokenKind):
        self.text = tokenText
        #  text used for identifiers, strings and numbers
        self.kind = tokenKind
        #  type the token is classified as

    @staticmethod
    def checkIfKeyword(keyword):
        for kind in TokenType:
            #  relies on all enum values being 1xx
            if kind.name == keyword and kind.value >= 100 and kind.value < 200:
                return kind
        return None

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
    GT = 210
    GTEQ = 211

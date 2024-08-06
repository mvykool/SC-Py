import sys
from lex import *

# Parser object keeps track of current token
# and checks if the code matches the grammar


class Parser:
    def __init__(self, lexer):
        self.lexer = lexer

        self.curToken = None
        self.peekToken = None
        self.nextToken()
        self.nextToken()  # call twice to initialize current and peek

    #  return token if current token matches
    def checkToken(self, kind):
        return kind == self.curToken.kind

    #  return token if next token matches
    def checkPeek(self, kind):
        return kind == self.peekToken.kind

    # Try to match current token. If not, error.
    # Advances the current token.
    def match(self, kind):
        if not self.checkToken(kind):
            self.abort("expected" + kind.name +
                       "got" + self.curToken.kind.name)
            self.nextToken()

    # advance current token
    def nextToken(self):
        self.curToken = self.peekToken
        self.peekToken = self.lexer.getToken()

    def abort(self, message):
        sys.exit("error" + message)

    #  Production rules

    #  program :: ={statement}

    def program(self):
        print("PROGRAM")

        #  parse all the statements in the program
        while not self.checkToken(TokenType.EOF):
            self.statement()

    #  one of the following statement

    def statement(self):
        #  check the first toekn to see what kind of statement it isinstance
        #  print (expression | string)
        if self.checkToken(TokenType.PRINT):
            print("STATEMENT-PRINT")
            self.nextToken()

            if self.checkToken(TokenType.STRING):
                #  simple string
                self.nextToken()
            else:
                #  expect an expression
                self.expression()

        #  new line
        self.nl()

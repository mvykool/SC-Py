import sys
from lex import *

# Parser object keeps track of current token
# and checks if the code matches the grammar


class Parser:
    def __init__(self, lexer):
        pass

    #  return token if current token matches
    def checkToken(self, kind):
        return kind == self.curToken.kind

    #  return token if next token matches
    def checkPeek(self, kind):
        return kind == self.peekToken.kind

    # Try to match current token. If not, error.
    # Advances the current token.
    def match(self, kind):
        pass

    # advance current token
    def nextToken(self):
        pass

    def abort(self, message):
        sys.exit("error" + message)

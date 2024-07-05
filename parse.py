import sys
from lex import *

# Parser object keeps track of current token
# and checks if the code matches the grammar


class Parser:
    def __init__(self, lexer):
        self.lexer = lexer

        self.symbols = set()
        self.labelsDeclared = set()
        self.labelsGotoed = set()

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

        #  newlines are required in our grammar
        while self.checkToken(TokenType.NEWLINE):
            self.nextToken()

        #  parse all the statements in the program
        while not self.checkToken(TokenType.EOF):
            self.statement()

        #  check that each label is referenced GOTO declared
        for label in self.labelsGotoed:
            if label not in self.labelsGotoed:
                self.abort("attempt to GOTO to undeclared label:" + label)

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

        # if statement comparison
        elif self.checkToken(TokenType.IF):
            print("STATEMENT-IF")
            self.nextToken()
            self.comparison()

            self.match(TokenType.THEN)
            self.nl()

            # zero or more statements
            while not self.checkToken(TokenType.ENDIF):
                self.statement()

            self.match(TokenType.ENDIF)

        #  while comparise and endwhile
        elif self.checkToken(TokenType.WHILE):
            print("STATEMENT-WHILE")
            self.nextToken()
            self.comparison()

            self.match(TokenType.REPEAT)
            self.nl()

            # zero or more statemnt in the loop
            while not self.checkToken(TokenType.ENDWHILE):
                self.statement()

            self.match(TokenType.ENDWHILE)

        #  LABEL ident
        elif self.checkToken(TokenType.LABEL):
            print("STATEMENT-LABEL")
            self.nextToken()

            #  make sure this label doesnt exist
            if self.curToken.text in self.labelsDeclared:
                self.abort("label already exist:" + self.curToken.text)
            self.labelsDeclared.add(self.curToken.text)

            self.match(TokenType.IDENT)

        #  GOTO ident
        elif self.checkToken(TokenType.GOTO):
            print("STATEMENT-GOTO")
            self.nextToken()
            self.labelsGotoed.add(self.curToken.text)
            self.match(TokenType.IDENT)

        #  LET ident expression
        elif self.checkToken(TokenType.LET):
            self.nextToken()

            # check if ident exist in symbol table, if not declare it
            if self.curToken.text not in self.symbols:
                self.symbols.add(self.curToken.text)

            self.match(TokenType.IDENT)
            self.match(TokenType.EQ)

            self.expression()

        #  INPUT Indent
        elif self.checkToken(TokenType.INPUT):
            self.nextToken()

            #  if variable doesnt exist already, declare it
            if self.curToken.text not in self.symbols:
                self.symbols.add(self.curToken.text)

            self.match(TokenType.IDENT)

        #  This is not a valid statement
        else:
            self.abort("Invalid statement" + self.curToken.text +
                       "(" + self.curToken.kind.name + ")")
        #  new line
        self.nl()

    #  nl ::='\n'+
    def nl(self):
        print("NEWLINE")

        #  require at least one NEWLINE
        self.match(TokenType.NEWLINE)

        #  but we will allow extra
        while self.checkToken(TokenType.NEWLINE):
            self.nextToken()

    #  comparison expressions
    def comparison(self):
        print("COMPARISON")

        self.expression()
        #  must be at least one com and another exp
        if self.isComparisonOperator():
            self.nextToken()
            self.expression()
        else:
            self.abort("expected comparison at:" + self.curToken.text)

        #  can have 0 or more comparison and expression
        while self.isComparisonOperator():
            self.nextToken()
            self.expression()

    #  return true if the current token is comparison
    def isComparisonOperator(self):
        return self.checkToken(TokenType.GT) or self.checkToken(TokenType.GTEQ) or self.checkToken(TokenType.LT) or self.checkToken(TokenType.LTEQ) or self.checkToken(TokenType.EQEQ) or self.checkToken(TokenType.NOTEQ)

    #  expressions term + -
    def expression(self):
        print("EXPRESSION")

        self.term()
        #  can have 0 or more +/- expressions
        while self.checkToken(TokenType.PLUS) or self.checkToken(TokenType.MINUS):
            self.nextToken()
            self.term()

    #  term unary / *
    def term(self):
        print("TERM")

        self.unary()
        # can have 0 or more * / expressions
        while self.checkToken(TokenType.ASTERISK) or self.checkToken(TokenType.SLASH):
            self.nextToken()
            self.unary()

    #  unary + - primary
    def unary(self):
        print("UNARY")

        #  optional unary + -
        if self.checkToken(TokenType.PLUS) or self.checkToken(TokenType.MINUS):
            self.nextToken()
        self.primary()

    #  primary number ident
    def primary(self):
        print("PRIMARY (" + self.curToken.text + ")")

        if self.checkToken(TokenType.NUMBER):
            self.nextToken()
        elif self.checkToken(TokenType.IDENT):
            # ensure the variable already exist
            if self.curToken.text not in self.symbols:
                self.abort("variable before assigment: " + self.curToken.text)
            self.nextToken()
        else:
            #  error
            self.abort("unexpected token at" + self.curToken.text)

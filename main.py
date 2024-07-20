from lex import *


def main():
    source = "LET foo = 123"
    lexer = Lexer(source)

    while lexer.peek() != '\0':
        print(lexer.curChar)
        lexer.nextChar()


main()

from lex import *


def main():
    source = "+- \"This is a string\" ~ This is a comment!\n */"
    lexer = Lexer(source)

    token = lexer.getToken()
    while token.kind != TokenType.EOF:
        print(token.kind)
        token = lexer.getToken()


main()

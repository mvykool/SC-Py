from lex import *


def main():
    source = "+- ~ this is a comment\n */"
    lexer = Lexer(source)

    token = lexer.getToken()
    while token.kind != TokenType.EOF:
        print(token.kind)
        token = lexer.getToken()


main()

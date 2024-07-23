from lex import *
from parse import *
import sys


def main():
    print("tenny compoiler")

    if len(sys.argv) != 2:
        sys.exit("error compiler needs source file as argument")
    with open(sys.argv[1], 'r') as inputFile:
        source = inputFile.read()

    #  initialize parser and Lexer
    lexer = Lexer(source)
    parser = Parser(lexer)

    parser.program()  # start parser
    print("print parser completed")


main()

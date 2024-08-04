from lex import *
from emit import *
from parse import *
import sys
import os


def main():
    print("tenny compoiler")

    if len(sys.argv) != 2:
        sys.exit("error compiler needs source file as argument")

    # adding strict type extension
    input_filename = sys.argv[1]
    if not input_filename.endswith('.rk'):
        sys.exit("error: source file must be .rk extension")

    with open(sys.argv[1], 'r') as inputFile:
        source = inputFile.read()

    #  initialize parser and Lexer
    lexer = Lexer(source)
    emitter = Emitter("out.c")
    parser = Parser(lexer, emitter)

    parser.program()  # start parser
    emitter.writeFile()  # write the output to file
    print("Compiling completed")

main()

from Tokenizer import Lexer
from Parser import Parser
from ASTPrinter import print_ast

with open("src.txt", 'r') as file:
    content= file.read()
lexer = Lexer(content)
tokens = lexer.tokenize()

print("=== TOKENS ===")
for token in tokens:
    print(f"Type: {token.type}, line: {token.line}, value: {token.value}") 

print("\n=== AST ===")
parser = Parser(tokens)
ast    = parser.parse()
print_ast(ast)

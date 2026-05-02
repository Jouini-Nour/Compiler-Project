from Tokenizer import Lexer
from Parser import Parser
from ASTPrinter import print_ast
from SemanticAnalyzer import SemanticAnalyzer

with open("tests/stress.txt", 'r') as file:
    content= file.read()

# 1) Lexical Analysis
lexer = Lexer(content)
tokens = lexer.tokenize()

print("=== TOKENS ===")
for token in tokens:
    print(f"Type: {token.type}, line: {token.line}, value: {token.value}") 

# 2) Syntax Analysis
print("\n=== AST ===")
parser = Parser(tokens)
ast    = parser.parse()
print_ast(ast)

# 3. Semantic Analysis
print("\n=== Semantic Analysis ===")
try:
    analyzer = SemanticAnalyzer()
    analyzer.analyze(ast)
    print("Semantic Analysis: Success (No errors found).")
except Exception as e:
    print(f"Semantic Analysis Error: {e}")
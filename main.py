from Tokenizer import Lexer

with open("src.txt", 'r') as file:
    content= file.read()
lexer = Lexer(content)
tokens = lexer.tokenize()
for token in tokens:
    print(f"Type: {token.type}, line: {token.line}, value: {token.value}") 
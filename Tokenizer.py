from TokenType import TokenType, KEYWORDS
from Token import Token

class Lexer:
    def __init__(self, src) -> None:
        self.src = src
        self.index= 0
    
    def tokenize(self):
        tokens = []
        buffer =[]
        line_count=1 

        while self.peek():
            # Skip whitespace
            if self.peek().isspace():
                if self.peek() == '\n':
                    line_count += 1
                self.consume()
                continue

            # Identifiers / KEYWORDS
            if(self.peek().isalpha()):
                buffer.append(self.consume())
                while (self.peek() and (self.peek().isalnum())):
                    buffer.append(self.consume())
                
                word = "".join(buffer)
                
                token_type = KEYWORDS.get(word, TokenType.IDENT)
                tokens.append(Token(token_type, line_count, word))
            
                buffer.clear()
                word=""
                continue
            
            # NUMBERS
            if (self.peek().isdigit()):
                buffer.append(self.consume())
                while(self.peek() and self.peek().isdigit()):
                    buffer.append(self.consume())
                
                tokens.append(Token(TokenType.INT_LIT, line_count, "".join(buffer)))
                buffer.clear()
                continue

            # Comments
            if (self.peek() == '/' and self.peek(1) and self.peek(1) == '/'):
                self.consume()
                self.consume()
                while(self.peek() and self.peek() != '\n'):
                    self.consume()
                continue

            if (self.peek() == '/' and self.peek(1) and self.peek(1) == '*'):
                self.consume()
                self.consume()
                while(self.peek()):
                    if(self.peek()=='*' and self.peek() and self.peek(1)=='/'):
                        self.consume()
                        self.consume()
                        break
                    self.consume()
                continue
            # STRINGS
            if self.peek() == '"':
                self.consume()  # Consume the opening "
                while self.peek() and self.peek() != '"':
                    # Handle newlines inside strings if your language allows it, 
                    # otherwise raise an error or increment line_count.
                    if self.peek() == '\n':
                        line_count += 1
                    buffer.append(self.consume())
    
                if self.peek() is None:
                    raise ValueError(f"Lexical Error: Unterminated string at line {line_count}")
        
                self.consume()  # Consume the closing "
    
                tokens.append(Token(TokenType.STRING_, line_count, "".join(buffer)))
                buffer.clear()
                continue

            # Single Character Tokens
            char = self.consume()
            if(char =='('):
                tokens.append(Token(TokenType.OPEN_PAREN, line_count))  
            elif(char =='='):
                tokens.append(Token(TokenType.EQ, line_count))
            elif(char ==')'):
                tokens.append(Token(TokenType.CLOSE_PAREN, line_count)) 
            elif(char =='{'):
                tokens.append(Token(TokenType.OPEN_CURLY, line_count)) 
            elif(char =='}'):
                tokens.append(Token(TokenType.CLOSE_CURLY, line_count)) 
            elif(char =='+'):
                tokens.append(Token(TokenType.PLUS, line_count)) 
            elif(char =='-'):
                tokens.append(Token(TokenType.MINUS, line_count)) 
            elif(char =='*'):
                tokens.append(Token(TokenType.STAR, line_count)) 
            elif(char =='/'):
                tokens.append(Token(TokenType.FSLASH, line_count)) 
            elif(char ==';'):
                tokens.append(Token(TokenType.SEMI, line_count)) 
            elif(char == '>'):
                tokens.append(Token(TokenType.SUP, line_count))
            elif(char == '<'):
                tokens.append(Token(TokenType.INF, line_count))
            else:
                raise ValueError(f"INVALID TOKEN at Line {line_count}: {char} ")
        self.index = 0
        return tokens
            
    def peek(self,offset=0) -> None | str:
        if (self.index + offset) >= len(self.src):
            return None
        return (self.src[self.index + offset])
    def consume(self):
        res = self.src[self.index]
        self.index+=1
        return res
    
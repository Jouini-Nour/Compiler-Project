from enum import Enum, auto
class TokenType(Enum):
   
    INT_LIT=auto()
    SEMI=2
    OPEN_PAREN=3
    CLOSE_PAREN=4
    IDENT=5
    EQ=6
    PLUS=7
    STAR=8
    MINUS=9
    FSLASH=10
    OPEN_CURLY=11
    CLOSE_CURLY=12
    IF_=13
    ELIF_=14
    ELSE_=15
    EXIT=16
    INT_ = 17
    SUP = 18
    INF = 19
    STRING_ = 20
KEYWORDS = {
    "exit": TokenType.EXIT,
    "int": TokenType.INT_,
    "string": TokenType.STRING_,
    "if": TokenType.IF_,
    "elif": TokenType.ELIF_,
    "else": TokenType.ELSE_,
}

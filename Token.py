from TokenType import TokenType
class Token:
    def __init__(self,type: TokenType, line: int, value: str = "" ) -> None:
        self.type = type
        self.line = line
        self.value = value
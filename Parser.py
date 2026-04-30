from TokenType import TokenType
from ASTNodes import (
    Program, DeclStmt, AssignStmt, IfStmt,
    Condition, BinOp, Ident, IntLit, StringLit
)

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index  = 0

    # -------------------------------------------------------
    # Helpers
    # -------------------------------------------------------

    def peek(self, offset=0):
        pos = self.index + offset
        if pos >= len(self.tokens):
            return None
        return self.tokens[pos]

    def consume(self):
        tok = self.tokens[self.index]
        self.index += 1
        return tok

    def expect(self, token_type):
        tok = self.peek()
        if tok is None or tok.type != token_type:
            line = tok.line if tok else "EOF"
            raise SyntaxError(
                f"Expected {token_type} but got "
                f"{tok.type if tok else 'EOF'} at line {line}"
            )
        return self.consume()

    # -------------------------------------------------------
    # Grammar:
    #
    # program     → stmt*
    # stmt        → decl_stmt | assign_stmt | if_stmt
    # decl_stmt   → ("int"|"string") IDENT ("=" expr)? ";"
    # assign_stmt → IDENT "=" expr ";"
    # if_stmt     → "if" "(" condition ")" "{" stmt* "}"
    #               ("elif" "(" condition ")" "{" stmt* "}")*
    #               ("else" "{" stmt* "}")?
    # condition   → expr (">" | "<" | "=") expr
    # expr        → term (("+"|"-") term)*
    # term        → factor (("*"|"/") factor)*
    # factor      → INT_LIT | IDENT | "(" expr ")"
    # -------------------------------------------------------

    def parse(self) -> Program:
        stmts = []
        while self.peek() is not None:
            stmts.append(self.stmt())
        return Program(stmts)

    def stmt(self):
        tok = self.peek()
        if tok is None:
            raise SyntaxError("Unexpected end of input")

        if tok.type in (TokenType.INT_, TokenType.STRING_):
            return self.decl_stmt()

        if tok.type == TokenType.IF_:
            return self.if_stmt()

        if tok.type == TokenType.IDENT:
            return self.assign_stmt()

        raise SyntaxError(
            f"Unexpected token {tok.type} ('{tok.value}') at line {tok.line}"
        )

    def decl_stmt(self):
        type_tok  = self.consume()          # "int" or "string"
        type_name = type_tok.value          # the actual string "int"/"string"
        name_tok  = self.expect(TokenType.IDENT)

        init_expr = None
        if self.peek() and self.peek().type == TokenType.EQ:
            self.consume()                  # consume "="
            init_expr = self.expr()

        self.expect(TokenType.SEMI)
        return DeclStmt(type_name, name_tok.value, init_expr)

    def assign_stmt(self):
        name_tok = self.expect(TokenType.IDENT)
        self.expect(TokenType.EQ)
        value = self.expr()
        self.expect(TokenType.SEMI)
        return AssignStmt(name_tok.value, value)

    def if_stmt(self):
        self.expect(TokenType.IF_)
        self.expect(TokenType.OPEN_PAREN)
        cond = self.condition()
        self.expect(TokenType.CLOSE_PAREN)
        self.expect(TokenType.OPEN_CURLY)
        body = self.block()
        self.expect(TokenType.CLOSE_CURLY)

        elifs = []
        while self.peek() and self.peek().type == TokenType.ELIF_:
            self.consume()
            self.expect(TokenType.OPEN_PAREN)
            elif_cond = self.condition()
            self.expect(TokenType.CLOSE_PAREN)
            self.expect(TokenType.OPEN_CURLY)
            elif_body = self.block()
            self.expect(TokenType.CLOSE_CURLY)
            elifs.append((elif_cond, elif_body))

        else_ = None
        if self.peek() and self.peek().type == TokenType.ELSE_:
            self.consume()
            self.expect(TokenType.OPEN_CURLY)
            else_ = self.block()
            self.expect(TokenType.CLOSE_CURLY)

        return IfStmt(cond, body, elifs, else_)

    def block(self):
        stmts = []
        while self.peek() and self.peek().type != TokenType.CLOSE_CURLY:
            stmts.append(self.stmt())
        return stmts

    def condition(self):
        left   = self.expr()
        op_tok = self.peek()
        if op_tok is None or op_tok.type not in (
            TokenType.SUP, TokenType.INF, TokenType.EQ
        ):
            line = op_tok.line if op_tok else "EOF"
            raise SyntaxError(f"Expected comparison operator at line {line}")
        op = self.consume().type
        right = self.expr()
        return Condition(left, op, right)

    def expr(self):
        node = self.term()
        while self.peek() and self.peek().type in (TokenType.PLUS, TokenType.MINUS):
            op    = self.consume().type
            right = self.term()
            node  = BinOp(op, node, right)
        return node

    def term(self):
        node = self.factor()
        while self.peek() and self.peek().type in (TokenType.STAR, TokenType.FSLASH):
            op    = self.consume().type
            right = self.factor()
            node  = BinOp(op, node, right)
        return node

    def factor(self):
        tok = self.peek()
        if tok is None:
            raise SyntaxError("Unexpected end of input in expression")

        if tok.type == TokenType.INT_LIT:
            self.consume()
            return IntLit(int(tok.value))

        if tok.type == TokenType.IDENT:
            self.consume()
            return Ident(tok.value)

        if tok.type == TokenType.OPEN_PAREN:
            self.consume()
            node = self.expr()
            self.expect(TokenType.CLOSE_PAREN)
            return node

        raise SyntaxError(
            f"Unexpected token {tok.type} ('{tok.value}') at line {tok.line}"
        )
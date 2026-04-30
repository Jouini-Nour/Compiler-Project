class Program:
    def __init__(self, stmts):
        self.stmts = stmts
    def __repr__(self):
        return f"Program({self.stmts})"

class DeclStmt:
    def __init__(self, type_, name, init_expr=None):
        self.type_     = type_
        self.name      = name
        self.init_expr = init_expr
    def __repr__(self):
        if self.init_expr:
            return f"Decl({self.type_} {self.name} = {self.init_expr})"
        return f"Decl({self.type_} {self.name})"

class AssignStmt:
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr
    def __repr__(self):
        return f"Assign({self.name} = {self.expr})"

class IfStmt:
    def __init__(self, cond, body, elifs, else_):
        self.cond  = cond
        self.body  = body
        self.elifs = elifs    # list of (Condition, [stmts])
        self.else_ = else_    # list of stmts or None
    def __repr__(self):
        return f"If({self.cond}, body={self.body}, elifs={self.elifs}, else={self.else_})"

class Condition:
    def __init__(self, left, op, right):
        self.left  = left
        self.op    = op
        self.right = right
    def __repr__(self):
        return f"Cond({self.left} {self.op} {self.right})"

class BinOp:
    def __init__(self, op, left, right):
        self.op    = op
        self.left  = left
        self.right = right
    def __repr__(self):
        return f"BinOp({self.left} {self.op} {self.right})"

class Ident:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"Ident({self.name})"

class IntLit:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f"Int({self.value})"

class StringLit:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f"Str({self.value})"
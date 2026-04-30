from ASTNodes import (
    Program, DeclStmt, AssignStmt, IfStmt,
    Condition, BinOp, Ident, IntLit, StringLit
)
from TokenType import TokenType

# Maps TokenType operators to readable symbols
OP_SYMBOLS = {
    TokenType.PLUS:  "+",
    TokenType.MINUS: "-",
    TokenType.STAR:  "*",
    TokenType.FSLASH: "/",
    TokenType.SUP:   ">",
    TokenType.INF:   "<",
    TokenType.EQ:    "=",
}

def print_ast(node, prefix="", is_last=True):
    """
    Recursively prints the AST as a tree.
    prefix  : the indentation string built up as we recurse
    is_last : whether this node is the last child of its parent
    """
    connector = "└── " if is_last else "├── "
    extension = "    " if is_last else "│   "

    if isinstance(node, Program):
        print("Program")
        for i, stmt in enumerate(node.stmts):
            print_ast(stmt, prefix, i == len(node.stmts) - 1)

    elif isinstance(node, DeclStmt):
        print(f"{prefix}{connector}Decl [{node.type_}] '{node.name}'")
        if node.init_expr:
            print_ast(node.init_expr, prefix + extension, is_last=True)

    elif isinstance(node, AssignStmt):
        print(f"{prefix}{connector}Assign '{node.name}'")
        print_ast(node.expr, prefix + extension, is_last=True)

    elif isinstance(node, IfStmt):
        print(f"{prefix}{connector}If")
        new_prefix = prefix + extension
        # condition
        has_more = bool(node.elifs) or node.else_ is not None
        print(f"{new_prefix}{'├── ' if (has_more or node.body) else '└── '}Condition")
        cond_prefix = new_prefix + ("│   " if (has_more or node.body) else "    ")
        _print_condition(node.cond, cond_prefix)
        # body
        body_is_last = not node.elifs and node.else_ is None
        print(f"{new_prefix}{'└── ' if body_is_last else '├── '}Body")
        body_prefix = new_prefix + ("    " if body_is_last else "│   ")
        for i, stmt in enumerate(node.body):
            print_ast(stmt, body_prefix, i == len(node.body) - 1)
        # elifs
        for idx, (elif_cond, elif_body) in enumerate(node.elifs):
            elif_is_last = (idx == len(node.elifs) - 1) and node.else_ is None
            print(f"{new_prefix}{'└── ' if elif_is_last else '├── '}Elif")
            elif_prefix = new_prefix + ("    " if elif_is_last else "│   ")
            print(f"{elif_prefix}├── Condition")
            _print_condition(elif_cond, elif_prefix + "│   ")
            print(f"{elif_prefix}└── Body")
            for i, stmt in enumerate(elif_body):
                print_ast(stmt, elif_prefix + "    ", i == len(elif_body) - 1)
        # else
        if node.else_ is not None:
            print(f"{new_prefix}└── Else")
            else_prefix = new_prefix + "    "
            for i, stmt in enumerate(node.else_):
                print_ast(stmt, else_prefix, i == len(node.else_) - 1)

    elif isinstance(node, BinOp):
        op_sym = OP_SYMBOLS.get(node.op, str(node.op))
        print(f"{prefix}{connector}BinOp '{op_sym}'")
        new_prefix = prefix + extension
        print_ast(node.left,  new_prefix, is_last=False)
        print_ast(node.right, new_prefix, is_last=True)

    elif isinstance(node, Ident):
        print(f"{prefix}{connector}Ident '{node.name}'")

    elif isinstance(node, IntLit):
        print(f"{prefix}{connector}Int {node.value}")

    elif isinstance(node, StringLit):
        print(f"{prefix}{connector}Str '{node.value}'")

    else:
        print(f"{prefix}{connector}Unknown({node})")


def _print_condition(cond, prefix):
    """Helper to print a Condition node's children under an existing 'Condition' label."""
    op_sym = OP_SYMBOLS.get(cond.op, str(cond.op))
    print(f"{prefix}├── op: '{op_sym}'")
    print(f"{prefix}├── left")
    print_ast(cond.left,  prefix + "│   ", is_last=True)
    print(f"{prefix}└── right")
    print_ast(cond.right, prefix + "    ", is_last=True)
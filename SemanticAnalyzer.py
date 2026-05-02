from SymbolTable import SymbolTable

class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = SymbolTable()

    def analyze(self, node):
        """Main entry point to start analysis"""
        return self.visit(node)

    def visit(self, node):
        """Dispatch method to call the correct visitor function"""
        method_name = f'visit_{type(node).__name__}'
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception(f"No visit_{type(node).__name__} method defined.")

    # --- Visiting Statements ---

    def visit_Program(self, node):
        for stmt in node.stmts:
            self.visit(stmt)

    def visit_DeclStmt(self, node):
        # Register the variable in the symbol table
        self.symbol_table.declare(node.name, node.type_)
    
        if node.init_expr:
            # Get the type of the expression (e.g., "string")
            expr_type = self.visit(node.init_expr)
        
            # Compare "int" (node.type_) vs "string" (expr_type)
            if node.type_ != expr_type:
                raise Exception(f"Semantic Error: Cannot initialize {node.type_} variable '{node.name}' with {expr_type} value.")

    def visit_AssignStmt(self, node):
        var_type = self.symbol_table.lookup(node.name)
        expr_type = self.visit(node.expr)
    
        if var_type != expr_type:
            raise Exception(f"Semantic Error: Cannot assign {expr_type} to variable '{node.name}' of type {var_type}.")

    def visit_IfStmt(self, node):
        # Check main IF
        self.visit(node.cond)
        self.symbol_table.enter_scope()
        for stmt in node.body:
            self.visit(stmt)
        self.symbol_table.exit_scope()

        # Check ELIFs
        for cond, body in node.elifs:
            self.visit(cond)
            self.symbol_table.enter_scope()
            for stmt in body:
                self.visit(stmt)
            self.symbol_table.exit_scope()

        # Check ELSE
        if node.else_:
            self.symbol_table.enter_scope()
            for stmt in node.else_:
                self.visit(stmt)
            self.symbol_table.exit_scope()

    # --- Visiting Expressions (These return a type string) ---

    def visit_IntLit(self, node):
        return "int"

    def visit_StringLit(self, node):
    # Returns the type 'string' so visit_DeclStmt can compare it
        return "string"

    def visit_Ident(self, node):
        return self.symbol_table.lookup(node.name)

    def visit_BinOp(self, node):
        left_type = self.visit(node.left)
        right_type = self.visit(node.right)
        
        # Simple rule: Math only allowed on integers
        if left_type == "int" and right_type == "int":
            return "int"
        
        raise Exception(f"Semantic Error: Binary operation {node.op} not supported between {left_type} and {right_type}")

    def visit_Condition(self, node):
        left_type = self.visit(node.left)
        right_type = self.visit(node.right)
        if left_type != right_type:
            raise Exception(f"Semantic Error: Cannot compare {left_type} with {right_type}")
        return "bool"
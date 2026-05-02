class SymbolTable:
    def __init__(self):
        # A list of dictionaries, where each dict is a scope level
        self.scopes = [{}] 

    def enter_scope(self):
        self.scopes.append({})

    def exit_scope(self):
        self.scopes.pop()

    def declare(self, name, type_):
        # Check if already declared in the CURRENT scope
        if name in self.scopes[-1]:
            raise Exception(f"Semantic Error: Variable '{name}' already declared in this scope.")
        self.scopes[-1][name] = type_

    def lookup(self, name):
        # Search from the inner-most scope outwards
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        raise Exception(f"Semantic Error: Variable '{name}' used before declaration.")
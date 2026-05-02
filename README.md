# Compiler Project

## 📌 Summary
This project is a functional compiler front-end developed for the Compiler Module. It translates source code into an Abstract Syntax Tree (AST) and performs rigorous semantic validation.

---

## 🏗️ Architecture
This compiler consists of three completed main steps:

1. **Lexer** ✅
2. **Parser** ✅
3. **Semantic Analysis** ✅

---

## 🏗️ Implementation Details

### Lexer
Implemented using a **character-by-character scanning approach** with a peek/consume mechanism.
* **Supports:** Identifiers, Integers, Strings, Arithmetic/Comparison operators, and Comments.
* **Tracking:** Precise line numbering for multi-line source files.

### Parser
A hand-written **Recursive Descent Parser** that transforms tokens into a hierarchical AST.
* **Operator Precedence:** Handled through grammar hierarchy (Factors → Terms → Expressions).
* **Control Flow:** Supports nested `if`, `elif`, and `else` blocks.

### Semantic Analysis
Ensures the program has meaningful, logical structure by traversing the AST using the **Visitor Pattern**.
* **Symbol Table:** A stack-based data structure that manages variable types and nested scope levels.
* **Type Checking:** Validates type compatibility in assignments and binary operations.
* **Scope Resolution:** Ensures variables are declared before use and handles block-level scoping.

---

## ⚙️ Grammar (C-style syntax)
```ebnf
program      →  stmt*
stmt         →  decl_stmt | assign_stmt | if_stmt
decl_stmt    →  ("int" | "string") IDENT ("=" expr)? ";"
assign_stmt  →  IDENT "=" expr ";"
if_stmt      →  "if" "(" condition ")" "{" stmt* "}"
                ("elif" "(" condition ")" "{" stmt* "}")*
                ("else" "{" stmt* "}")?
condition    →  expr (">" | "<" | "=") expr
expr         →  term (("+"|"-") term)*
term         →  factor (("*"|"/") factor)*
factor       →  INT_LIT | STRING_LIT | IDENT | "(" expr ")"
```

## 🧪 Semantic Validation Example
Input (src.txt):
```c
int x = 10;
if (x > "hello") {
    string test = "world";
}
```

Analysis Result:
The compiler performs a recursive walk of the AST and catches the logical error:

```bash
=== AST ===
Program
└── If
    ├── Condition
    │   ├── left: Int 10
    │   └── right: Str 'hello'
    └── Body ...

=== Semantic Analysis ===
Semantic Analysis Error: Semantic Error: Cannot compare int with string
```

Key Error Checks:
* Type Mismatch: `int x = "string";` → Raises Error.
* Incompatible Ops: `10 + "hello"` → Raises Error.
* Out of Scope: Accessing a variable declared inside an if block from the outside → Raises Error.

---

## 🧪 Testing Suite

The `tests/` directory contains various test scripts to verify the semantic analysis:

- `valid.txt`: Valid code that should pass analysis
- `type_mismatch.txt`: Tests for type mismatch errors
- `comp_mismatch.txt`: Tests for comparison mismatches
- `mixed_op.txt`: Tests for mixed operations
- `scope.txt`: Tests for scope resolution
- `undeclared.txt`: Tests for undeclared variables
- `stress.txt`: Stress tests for complex scenarios

These files help ensure the compiler correctly identifies and reports semantic errors.

---

## 🚀 Future Improvements
* Code Generation: Targeting an Intermediate Representation (IR) or Assembly.
* Enhanced Types: Support for float and boolean logic.
* Advanced Ops: Support for ==, !=, <=, and >=.
* Optimization: Constant folding and dead code elimination.

---

## 🛠️ How to Run
Place your source code in src.txt.

Execute the main driver:

```bash
python main.py
```

---

## 👥 Contributors
* Jouini Nour Elhak
* Ayadi Roua
* Mouhib Bahri
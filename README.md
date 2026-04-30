# Compiler Project

## 📌 Summary
This project is part of our Compiler Module requirements.

---

## 🏗️ Architecture
This compiler consists of three main steps:

1. **Lexer** ✅
2. **Parser** ✅
3. **Semantic Analysis**

---

## 🚧 Current State
The **Lexer** and **Parser** have been implemented and tested on small source code samples.

### Lexer supports:
* Keywords (`int`, `string`, `if`, `elif`, `else`, `exit`)
* Identifiers
* Integer literals
* Arithmetic operators (`+`, `-`, `*`, `/`)
* Comparison operators (`>`, `<`)
* Delimiters (`;`, `{}`, `()`)
* Comments:
  * Single-line (`//`)
  * Multi-line (`/* ... */`)
* Line number tracking for error reporting

### Parser supports:
* Variable declarations with optional initialization (`int x = 5;`)
* Variable assignments (`x = x + 1;`)
* Arithmetic expressions with correct precedence (`+`, `-`, `*`, `/`)
* Parenthesized expressions
* Conditional statements (`if`, `elif`, `else`)
* AST tree construction and pretty-printing

---

## ⚙️ Lexer Design

The lexer is implemented using a **character-by-character scanning approach** with a peek/consume mechanism.

### Key Features:
* Lookahead using `peek()`
* Controlled traversal using `consume()`
* Buffer-based token construction
* Keyword recognition
* Comment skipping
* Error handling for invalid tokens

---

## ⚙️ Parser Design

The parser is a hand-written **Recursive Descent Parser** that directly consumes the token list produced by the lexer.

### Key Features:
* Mirrors grammar rules as functions (`stmt()`, `expr()`, `term()`, `factor()`)
* Same peek/consume pattern as the Lexer for consistency
* Builds an **Abstract Syntax Tree (AST)** from tokens
* Handles operator precedence naturally through the grammar hierarchy
* Descriptive `SyntaxError` messages with line numbers

### Grammar (C-style syntax):

```
program     →  stmt*

stmt        →  decl_stmt
            |  assign_stmt
            |  if_stmt

decl_stmt   →  ("int" | "string") IDENT ("=" expr)? ";"

assign_stmt →  IDENT "=" expr ";"

if_stmt     →  "if" "(" condition ")" "{" stmt* "}"
               ("elif" "(" condition ")" "{" stmt* "}")*
               ("else" "{" stmt* "}")?

condition   →  expr (">" | "<" | "=") expr

expr        →  term (("+"|"-") term)*

term        →  factor (("*"|"/") factor)*

factor      →  INT_LIT
            |  IDENT
            |  "(" expr ")"
```

### Operator Precedence (low → high):

| Level | Operators | Rule   |
|-------|-----------|--------|
| 1     | `+`, `-`  | `expr` |
| 2     | `*`, `/`  | `term` |
| 3     | literals, identifiers, `(...)` | `factor` |

---

## 🧪 Example

### Input:
```c
int x = 5;
if (x > 2) {
    x = x + 1;
}
```

### Token Output:
```
INT_          | line 1 | value: 'int'
IDENT         | line 1 | value: 'x'
EQ            | line 1 | value: ''
INT_LIT       | line 1 | value: '5'
SEMI          | line 1 | value: ''
IF_           | line 2 | value: 'if'
OPEN_PAREN    | line 2 | value: ''
IDENT         | line 2 | value: 'x'
SUP           | line 2 | value: ''
INT_LIT       | line 2 | value: '2'
CLOSE_PAREN   | line 2 | value: ''
OPEN_CURLY    | line 2 | value: ''
IDENT         | line 3 | value: 'x'
EQ            | line 3 | value: ''
IDENT         | line 3 | value: 'x'
PLUS          | line 3 | value: ''
INT_LIT       | line 3 | value: '1'
SEMI          | line 3 | value: ''
CLOSE_CURLY   | line 4 | value: ''
```

### AST Output:
```
Program
├── Decl [int] 'x'
│   └── Int 5
└── If
    ├── Condition
    │   ├── op: '>'
    │   ├── left
    │   │   └── Ident 'x'
    │   └── right
    │       └── Int 2
    └── Body
        └── Assign 'x'
            └── BinOp '+'
                ├── Ident 'x'
                └── Int 1
```

---

## 🧩 Next Steps

### Semantic Analysis
* Type checking (e.g. no assigning strings to int variables)
* Variable scope validation (use before declaration)
* Symbol table implementation
* Semantic error messages with line numbers

---

## 🚀 Future Improvements
* Support additional data types (`float`, `boolean`)
* Multi-character operators (`==`, `!=`, `<=`, `>=`)
* Improved error messages with precise locations
* Intermediate code generation

---

## 🛠️ How to Run

```bash
git clone <repo-url>
cd <project-folder>
python main.py
```

---

## 📚 Learning Objectives
* Understand compiler design fundamentals
* Implement lexical analysis
* Learn parsing techniques
* Apply semantic validation

---

## 👥 Contributors
* Jouini Nour Elhak
* Ayadi Roua
* Mouhib Bahri
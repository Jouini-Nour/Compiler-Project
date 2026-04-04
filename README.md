# Compiler Project

## 📌 Summary

This project is part of our Compiler Module requirements.

---

## 🏗️ Architecture

This compiler consists of three main steps:

1. **Lexer**
2. **Parser**
3. **Semantic Analysis**

---

## 🚧 Current State

Only the **Lexer** has been implemented and tested on small source code samples.

It currently supports:

* Keywords (`int`, `if`, `elif`, `else`, `exit`)
* Identifiers
* Integer literals
* Arithmetic operators (`+`, `-`, `*`, `/`)
* Delimiters (`;`, `{}`, `()`)
* Comments:

  * Single-line (`//`)
  * Multi-line (`/* ... */`)

The lexer also tracks line numbers for better error reporting.

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

## 🧪 Example

### Input:

```c
int x = 10;
```

### Output:

```
(INT, line 1)
(IDENT, x, line 1)
(EQUALS, line 1)
(INT_LIT, 10, line 1)
(SEMI, line 1)
```

---

## 🧩 Next Steps

### 1. Parser (Syntax Analysis)

* Convert tokens into an **Abstract Syntax Tree (AST)**
* Validate syntax using a **Context-Free Grammar (CFG)**
* Detect syntax errors

### 2. Semantic Analysis

* Type checking
* Variable scope validation
* Ensure semantic correctness

---

## 🚀 Future Improvements

* Support additional data types (float, string, boolean)
* Multi-character operators (`==`, `!=`, `<=`, `>=`)
* Improved error messages with precise locations
* Symbol table implementation
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

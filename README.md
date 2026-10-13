# Stack-Based Expression Evaluator

## Student Project

This project is a Python-based mathematical expression evaluator
that uses the Stack data structure to evaluate arithmetic expressions.

## Objective

The objective of this project is to demonstrate the use of a Stack
data structure in evaluating mathematical expressions while following
operator precedence and handling parentheses.

## Data Structure Used

The main data structure used in this project is a Stack.

A Stack follows the LIFO principle:

Last In, First Out.

The Stack class contains the following operations:

- push() - adds an item to the stack.
- pop() - removes and returns the top item.
- peek() - returns the top item without removing it.
- is_empty() - checks whether the stack is empty.
- size() - returns the number of items in the stack.

## Operators Supported

The program supports the following arithmetic operators:

- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)

The program also supports parentheses.

## Operator Precedence

The program follows normal arithmetic precedence:

1. Multiplication (*) and Division (/)
2. Addition (+) and Subtraction (-)

Parentheses are evaluated first.

## Input

The program reads mathematical expressions from `input.txt`.

Expressions are separated using:

-----

Example:

3 + 5 * 2
-----
( 8 / 4 ) + 7 * 2
-----
10 - ( 2 + 3 ) * 4

## Output

The results are written to `output.txt`.

Example:

13
-----
16
-----
-10

## How to Run

Make sure Python is installed on the computer.

Open the project folder in VS Code and run:

```bash
python main.py
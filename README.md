# e-calc 
Python script for evaluating circuit/electrical engineering calculations.

## Features
- Capable of evaluatuating **complex expressions**, making AC analysis quick
and easy
- Many [functions](docs/functions.md) for common uses in circuit analysis
- CLI-based for fast startup
- Macros for SI unit values ('1k' = 1000, '1M' = 1000000)

I made this for my Electric Circuits exam, and it made calculations extremely 
quick and easy.

## Example Usage

Here it is evaluating a circuit analysis practice question:

![Example Usage](docs/term_recording.gif)


## Install

```
git clone git@github.com:Davis-Rippon/e-calc.git
pip install -e .
```
(You can also use ```pipx install -e .```)

After that you should see:
```
Installing to existing venv 'ecalc'
  installed package ecalc 0.1.0, installed using Python 3.13.3
  These apps are now globally available
    - e-calc
done! ✨ 🌟 ✨
```
Then just type ```e-calc``` and it will run

## Some High-Level Details
e-calc takes an expression:
```python
vdiv(1 | 2, -5/(2j + 3), toCart(5, cos, 90))
```

Tokenises it (through a custom lexer):
```python
[')', ')', 90.0, ',', 'cos', ',', 5.0, '(', 'toCart', ',', ')', 3.0, '+', 'j', 2.0, '(', '/', 5.0, '*', -1.0, ',', 2.0, '|', 1.0, '(', 'vdiv']
```
_Note: It's reversed as division is left-associative, i.e. 1/2/2 = (1/2)/2, not 1/(2/2)_

Then grammar rules are applied, defined recursively as follows:

```
        rules                                       python
        S -> expr                                   -

        expr -> expr + expr                         add(expr, expr)
        expr -> expr / expr                         divide(expr, expr)
        expr -> expr - expr                         subtract(expr, expr)
        expr -> expr | expr                         parallel(expr, expr)
        expr -> ( expr )                            return expr

        expr -> function(arg|STR, arg|STR, ...)     function(arg|STR, arg|STR, ...)

        arg -> expr                                 -
        arg -> STR                                  -

        expr ->  number                             -
        expr ->  cnumber                            -

        number -> CNUM                              return Complex(number)
        cnumber -> CNUM                             return Complex(0, number)
```
Applying these rules reduces expressions to a CNUM object, which is just a complex
number.

```
0.11111111 0.11111111j
```

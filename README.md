# e-calc 
Python script for evaluating circuit/electrical engineering calculations.

## Features
- Capable of evaluatuating **complex expressions**, making 
- Many [functions](#Functions) for common uses in circuit analysis
- CLI-based for quick

I made this for my Electric Circuits exam, and it made 

## Example Usage

Here it is evaluating a circuit analysis practice question:

![Example Usage](images/term_recording.gif)

## Functions

### `toCart(magnitude, "cos" or "sin", phase (degrees))`
Convert a sinusoid to its Cartesian complex equivalent.

Example: `toCart(10, sin, -90)`

---

### `vdiv(Voltage, r1, r2)`
Do a voltage divider, finding the voltage across `r1`.

---

### `toPhasor(expr)`
Print the Phasor representation of a complex number value.

---

### `cdiv(Current, r1, r2)`
Do a current divider, finding the current across `r1`.

---

### `pow(x, y)`
Compute `x^y`.

---

### `capz(frequency, capacitance)`
Find the impedance of a capacitor.

---

### `indz(frequency, inductance)`
Find the impedance of an inductor.

---

### `mag(expr)`
Find the magnitude of `expr`.

---

### `conj(expr)`
Find the complex conjugate of `expr`.

## Install

git clone git@github.com:Davis-Rippon/e-calc.git
python 


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

# e-calc 
Python script for evaluating circuit/electrical engineering calculations. To be used in exams!

## Example Usage

Here it is evaluating a circuit analysis practice question:

![Example Usage](images/term_recording.gif)

## Some High-Level Details
e-calc takes an expression:
```
vdiv(1 | 2, -5/(2j + 3), toCart(5, cos, 90))
```

Tokenises it (through a custom parser):
```
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

        expr -> function (arg, arg, ...)            function(arg, arg, ...)

        arg -> expr                                 -

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

from decimal import Decimal, getcontext


class Complex:
    def __init__(self, Re:float=0, Im:float=0):
        self.real = Decimal(Re)
        self.imag = Decimal(Im)

        # self.tolerance = Complex(10**-10)


    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)

    def __truediv__(self, other):
        denom = other.real**2 + other.imag**2
        if denom == 0:
            raise ZeroDivisionError("division by zero")
        real = (self.real * other.real + self.imag * other.imag) / denom
        imag = (self.imag * other.real - self.real * other.imag) / denom
        return Complex(real, imag)
    
    def __or__(self, other):
        # if (Complex(1)/self + Complex(1)/other) - self.tolerance < Complex(0): 
        #     return 0
        # TODO implement comparison

        return Complex(1)/(Complex(1)/self + Complex(1)/other)

    def __str__(self):
        real = self.real.quantize(Decimal('0.00000001'))
        imag = self.imag.quantize(Decimal('0.00000001'))

        re = f'{real}' if self.real != 0 else ""
        im = str(imag) + 'j' if self.imag != 0 else ""

        return f"{re} {im}"

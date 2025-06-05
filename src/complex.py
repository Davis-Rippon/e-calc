class Complex:
    def __init__(self, Re:float=0, Im:float=0):
        self.real = Re
        self.imag = Im


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
        return Complex(1)/(Complex(1)/self + Complex(1)/other)

    def __str__(self):
        re = str(self.real) if self.real != 0 else ""
        im = str(self.imag) + 'j' if self.imag != 0 else ""

        return f"{re} {im}"

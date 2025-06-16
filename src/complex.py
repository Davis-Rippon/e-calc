from decimal import Decimal, getcontext
import math

getcontext().prec = 100

class Complex:
    def __init__(self, Re:float=0, Im:float=0):
        self.real = Decimal(Re)
        self.imag = Decimal(Im)



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
    


    def magnitude(self):
        mag_squared = self.real.quantize(Decimal("0.000000000001")) ** 2 + self.imag.quantize(Decimal("0.000000000001")) ** 2
        return Complex(float(mag_squared.sqrt()))
        return 1

    def angle(self):
        # angle = atan2(im, re)
        return Decimal(math.atan2(float(self.imag), float(self.real)))

    def log(self):
        # complex logarithm: log(z) = ln|z| + i * arg(z)
        mag = self.magnitude().real
        ang = self.angle()
        return Complex(math.log(float(mag)), float(ang))

    def exp(self):
        # complex exponential: exp(a + ib) = exp(a) * (cos b + i sin b)
        exp_real = math.exp(float(self.real))
        return Complex(
            exp_real * math.cos(float(self.imag)),
            exp_real * math.sin(float(self.imag))
        )

    def conjugate(self):
        return Complex(float(self.real), float(-self.imag))

    def __pow__(self, power):
        if not isinstance(power, Complex):
            # allow power by real numbers for convenience
            power = Complex(power, 0)

        # z^w = exp(w * log(z))
        log_self = self.log()
        power_log = power * log_self
        return power_log.exp()


    def __or__(self, other):
        # if (Complex(1)/self + Complex(1)/other) - self.tolerance < Complex(0): 
        #     return 0
        # TODO implement comparison

        return Complex(1)/(Complex(1)/self + Complex(1)/other)

    def __str__(self):
        real = self.real.quantize(Decimal('0.000000000001'))
        imag = self.imag.quantize(Decimal('0.000000000001'))

        re = f'{real}' if self.real != 0 else ""
        im = str(imag) + 'j' if self.imag != 0 else ""

        return f"{re} {im}"

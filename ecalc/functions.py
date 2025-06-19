from decimal import Decimal
import math
from .complex import Complex


def toCart(amplitude:Complex = Complex(1), sinusoid:str="cos", phaseDeg:Complex=Complex(0)):
    if sinusoid == "sin": phaseDeg -= 90 # convert to cos if sin
    amp = float(amplitude.real)
    phdeg = math.radians(phaseDeg.real) # convert to radians
    return Complex(amp*math.cos(phdeg), amp*math.sin(phdeg))

def mag(v:Complex):
    return v.magnitude()

def toPhasor(v:Complex= Complex(0,0)):
    """
    Prints Phasor representation of complex number

    v: complex numbre
    returns: None
    """

    mag = v.magnitude()
    angle = (v.angle()*Decimal(180)/Decimal(math.pi)).quantize(Decimal("0.001"))

    # if angle > 90:
    #     angle -= 90
    #
    # elif angle <= -90:
    #     angle += 90

    print(f"Polar Form: {mag} ∠ {angle}°")
    return v

def vdiv(v, r1, r2):
    """
    r1: resistance
    r2: resistance
    returns: voltage across r1
    """
    return v*(r1/(r1 + r2))

def cdiv(c, r1, r2):
    """
    r1: resistance
    r2: resistance
    returns: current across r1
    """
    return c*(r2/(r1 + r2))

def pow(v1, v2):
    return v1 ** v2


def conj(v1:Complex):
    return v1.conjugate()

def capz(frequency:Complex, capacitance:Complex):
    return Complex(1,0)/(frequency*capacitance*Complex(0,1))

def indz(frequency:Complex, inductance:Complex):
    return frequency*inductance*Complex(0,1)

FUNCTIONS_TABLE = [("toCart", toCart), 
                   ("vdiv", vdiv),
                   ("toPhasor", toPhasor),
                   ("cdiv", cdiv),
                   ("pow", pow),
                   ("capz", capz),
                   ("indz", indz),
                   ("mag", mag),
                   ("con", conj),
                   ("cos", math.cos),
                   ("sin", math.sin)]

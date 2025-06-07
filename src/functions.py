import math
from .complex import Complex


def toCart(amplitude:Complex = Complex(1), sinusoid:str="cos", phaseDeg:Complex=Complex(0)):
    if sinusoid == "sin": phaseDeg -= 90 # convert to cos if sin
    amp = float(amplitude.real)
    phdeg = math.radians(phaseDeg.real) # convert to radians
    return Complex(amp*math.cos(phdeg), amp*math.sin(phdeg))

def toPhasor(v:Complex= Complex(0,0)):
    """
    Prints Phasor representation of complex number

    v: complex numbre
    returns: None
    """
    im = v.imag
    re = v.real

    mag = math.hypot(im, re)
    angle = math.atan2(im, re)*180/math.pi

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

FUNCTIONS_TABLE = [("toCart", toCart), 
                   ("vdiv", vdiv),
                   ("toPhasor", toPhasor),
                   ("cdiv", cdiv),
                   ("cos", math.cos),
                   ("sin", math.sin)]

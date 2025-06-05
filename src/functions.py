import math
from .complex import Complex


def toCart(amplitude:float = 1, sinusoid:str="cos", phaseDeg:float=0):
    if sinusoid == "sin": phaseDeg -= 90 # convert to cos if sin
    phaseDeg = math.radians(phaseDeg) # convert to radians
    return Complex(amplitude*math.cos(phaseDeg), amplitude*math.sin(phaseDeg))

def vdiv(r1, r2, v):
    return v*(r2/r1 + r2)

FUNCTIONS_TABLE = [("toCart", toCart), 
                   ("vdiv", vdiv)]

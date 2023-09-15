from numpy import exp, abs, angle

def polar2z(r,theta):
    return r * exp( 1j * theta )

def z2polar(z):
    return ( abs(z), angle(z) )


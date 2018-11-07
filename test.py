import numpy as np

def circle_circumference(r):
    """A function that calculates the circumference of a cirle with radius r"""
    return 2*np.pi*r

print(circle_circumference(1))

def circle_surface(r):
    """circle_surface(r) returns the surface of a circle of radius r"""
    return np.pi*r**2

print(circle_surface(1))

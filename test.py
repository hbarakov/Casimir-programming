import numpy as np

def circle_circumference(r):
    """circle_circumference(r) returns the circumference of a circle of radius r"""
    return 2*np.pi*r

print(circle_circumference(1))

def circle_surface(r):
    """circle_surface(r) returns the surface of a circle of radius r"""
    return np.pi*r**2

print(circle_surface(1))

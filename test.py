import numpy as np

def circle_circumference(r):
    """A function that calculates the circumference of a cirle with radius r"""
    return 2*np.pi*r

print(circle_circumference(1))

def circle_surface(r):
    """A function that calculates the surface area of a circle with radius r  """
    return np.pi*r**2

print(circle_surface(1))

import numpy as np

def circle_circumference(r):
    return 2*np.pi*r

print(circle_circumference(1))

def circle_surface(r):
    return np.pi*r**2

print(circle_surface(1))

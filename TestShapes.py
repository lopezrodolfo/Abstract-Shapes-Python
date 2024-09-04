"""
TestShapes.py

This file is used to test the functionality of the AbstractShapes module. 
It creates instances of different shapes such as Circle, Ellipse, Triangle, and Rectangle, 
and performs various operations on them, such as printing their details, 
comparing their names, and checking for equality and ordering.

Author: Rodolfo Lopez
"""

import AbstractShapes

if __name__ == "__main__":
    oval_1 = AbstractShapes.Circle("Wheel", 4)
    print(oval_1)
    oval_2 = AbstractShapes.Circle("Round", 4)
    print(oval_2)
    oval_3 = AbstractShapes.Circle("Hub", 3)
    print(oval_3)

    oval_4 = AbstractShapes.Ellipse("Disc", 6, 3)
    print(oval_4)
    oval_5 = AbstractShapes.Ellipse("Orb", 3, 6)
    print(oval_5)

    poly_1 = AbstractShapes.Triangle("Trinity", 4, 6, 3, 4, 5)
    print(poly_1)
    poly_2 = AbstractShapes.Rectangle("Box", 4, 3)
    print(poly_2)

    print(oval_1.name, "==", oval_2.name, oval_1 == oval_2)
    print(oval_1.name, "==", oval_3.name, oval_1 == oval_3)
    print(oval_4.name, "==", oval_5.name, oval_4 == oval_5)
    print(poly_2.name, "==", poly_1.name, poly_2 == poly_1)
    print(poly_1.name, "==", oval_3.name, poly_1 == oval_3)
    print(oval_3.name, "==", oval_1.name, oval_3 < oval_1)
    print(poly_1.name, "==", poly_2.name, poly_1 < poly_2)

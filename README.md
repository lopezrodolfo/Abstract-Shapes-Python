# AbstractShapes Module

## Overview

The `AbstractShapes` module provides an abstract base class for different geometric shapes and their implementations, including `Circle`, `Ellipse`, `Triangle`, and `Rectangle`. It allows for the creation of shape instances, calculation of their area and perimeter, and comparison of shapes based on their properties.

## Author

Rodolfo Lopez

## Date

Fall 2021

## Classes

### Shape (Abstract Base Class)

- **Methods:**
  - `area()`: Abstract method to calculate the area of the shape.
  - `perimeter()`: Abstract method to calculate the perimeter of the shape.

### Polygon (Inherits from Shape)

- **Methods:**
  - Inherits `area()` and `perimeter()` as abstract methods.

### Oval (Inherits from Shape)

- **Methods:**
  - Inherits `area()` and `perimeter()` as abstract methods.

### Rectangle (Inherits from Polygon)

- **Constructor:** `__init__(name, length, width)`
- **Methods:**
  - `area()`: Calculates the area of the rectangle.
  - `perimeter()`: Calculates the perimeter of the rectangle.
  - `__eq__(other)`: Compares two rectangles for equality based on area.
  - `__lt__(other)`: Compares two rectangles based on area.

### Triangle (Inherits from Polygon)

- **Constructor:** `__init__(name, base, height, a, b, c)`
- **Methods:**
  - `area()`: Calculates the area of the triangle.
  - `perimeter()`: Calculates the perimeter of the triangle.
  - `__eq__(other)`: Compares two triangles for equality based on area.
  - `__lt__(other)`: Compares two triangles based on area.

### Ellipse (Inherits from Oval)

- **Constructor:** `__init__(name, a, b)`
- **Methods:**
  - `area()`: Calculates the area of the ellipse.
  - `perimeter()`: Calculates the perimeter of the ellipse.
  - `__eq__(other)`: Compares two ellipses for equality based on area.
  - `__lt__(other)`: Compares two ellipses based on area.

### Circle (Inherits from Oval)

- **Constructor:** `__init__(name, radius)`
- **Methods:**
  - `area()`: Calculates the area of the circle.
  - `perimeter()`: Calculates the perimeter of the circle.
  - `__eq__(other)`: Compares two circles for equality based on area.
  - `__lt__(other)`: Compares two circles based on area.

## Usage

To test the functionality of the `AbstractShapes` module, run the `TestShapes.py` script. It creates instances of various shapes, prints their details, and compares them.

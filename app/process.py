import sys
import os
import numpy as np
import re

def parse_equations(equations):
    """Mengubah daftar persamaan menjadi matriks A dan vektor b."""
    A = []
    b = []
    for eq in equations:
        # Menghapus spasi
        eq = eq.replace(" ", "")

        # Memisahkan kiri dan kanan "="
        left, right = eq.split("=")
        right = float(right)

        # Membuat daftar koefisien [x, y, z]
        coefficients = [0, 0, 0]
        terms = re.findall(r'([+-]?\d*\.?\d*)([xyz])', left)
        print(terms)
        for coef, var in terms:
            if coef == '' or coef == '+':
                coef = 1.0
            elif coef == '-':
                coef = -1.0
            else:
                coef = float(coef)

            if var == 'x':
                coefficients[0] = coef
            elif var == 'y':
                coefficients[1] = coef
            elif var == 'z':
                coefficients[2] = coef

        A.append(coefficients)
        b.append(right)

    return (np.array(A), np.array(b))

def round_based_tolerance(x, tolerance):
    str_x = str(tolerance)
    if '.' in str_x:
        decimal_part = str_x.split('.')[1]
        number_of_digit = len(decimal_part) - 1

        if (number_of_digit < 0):
            return np.round(x, 0)
        
        return np.round(x, number_of_digit)
    else:
        return np.round(x, 0)


def jacobi_with_relative_error(A, b, x0, tolerance, max_iterations):
    n = len(b)
    x = x0.copy()
    results = []

    for i in range(max_iterations):
        x_new = np.zeros_like(x)

        for j in range(n):
            s = sum(A[j][k] * x[k] for k in range(n) if k != j)
            x_new[j] = (b[j] - s) / A[j][j]

        x_new = np.round(x_new, 14)
        relative_errors = np.where(x_new != 0, np.abs((x_new - x) / x_new) * 100, 0)
        relative_errors = np.round(relative_errors, 14)

        results.append((i + 1, *np.round(x_new, 3), *round_based_tolerance(relative_errors, tolerance)))

        if np.all(relative_errors < tolerance):
            break

        x = x_new

    return results
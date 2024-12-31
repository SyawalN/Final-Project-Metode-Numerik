from .process import parse_equations, jacobi_with_relative_error, np
from flask import (Blueprint, render_template, jsonify, request)

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/api/calculate', methods=['POST', 'GET'])
def calculate():
    if request.method == 'POST':
        data = request.get_json()
        equations = list(data.values())

        try:
            # Parsing persamaan menjadi A dan b
            A, b = parse_equations(equations)
            # print(f"A: {A}\nB: {b}")

            # Parameter metode Jacobi
            x0 = np.zeros_like(b)  # Tebakan awal
            tolerance = 0.05  # Toleransi
            max_iterations = 50  # Iterasi maksimum

            # Menyelesaikan dengan metode Jacobi
            results = jacobi_with_relative_error(A, b, np.array(x0), tolerance, max_iterations)
            return results
        except Exception as e:
            error_message = f"Terjadi kesalahan: {e}"
            return error_message

    return render_template('index.html')
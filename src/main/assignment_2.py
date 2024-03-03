import numpy as np


def neville_interpolation(target, x_values, y_values, degree):
    n = len(x_values)
    neville_table = np.zeros((n, n))
    for i in range(n):
        neville_table[i, 0] = y_values[i]
    for i in range(1, n):
        for j in range(1, i + 1):
            neville_table[i, j] = (
                (target - x_values[i - j]) * neville_table[i, j - 1]
                - (target - x_values[i]) * neville_table[i - 1, j - 1]
            ) / (x_values[i] - x_values[i - j])
    return neville_table[degree, n - 1]


def newton_forward_differences(x_values, y_values):
    n = len(x_values)
    differences_table = np.zeros((n, n))
    for i in range(n):
        differences_table[i][0] = y_values[i]

    for i in range(1, n):
        for j in range(1, i + 1):
            left_difference = differences_table[i][j - 1]
            upper_left_difference = differences_table[i - 1][j - 1]
            denominator = x_values[i] - x_values[i - j]
            differences_table[i][j] = (
                left_difference - upper_left_difference
            ) / denominator

    return differences_table


def newton_interpolation(x_values, y_values, target, degree, differences_table):
    result = differences_table[0][0]
    temp = 1
    for i in range(1, degree + 1):
        temp *= target - x_values[i - 1]
        product = temp * differences_table[i][i]
        result += product

    return result


def hermite_differences_table(x_values, y_values, derivatives):
    n = len(x_values)
    m = (2 * n) - 1
    differences_table = np.zeros((m + 1, m))

    for i in range(n):
        differences_table[2 * i][0] = x_values[i]
        differences_table[2 * i + 1][0] = x_values[i]
        differences_table[2 * i][1] = y_values[i]
        differences_table[2 * i + 1][1] = y_values[i]

    differences_table[1][2] = derivatives[0]

    for i in range(1, m + 1):
        for j in range(2, i + 2):
            if j > m - 1:
                continue
            if j == 2 and i % 2 == 1:
                differences_table[i][j] = derivatives[(i - 1) // 2]
            else:
                if i % 2 == 1:
                    differences_table[i][j] = (
                        differences_table[i][j - 1] - differences_table[i - 1][j - 1]
                    ) / (x_values[i // 2] - x_values[((i) - j) // 2])
                else:
                    differences_table[i][j] = (
                        differences_table[i][j - 1] - differences_table[i - 1][j - 1]
                    ) / (x_values[i // 2] - x_values[((i + 1) - j) // 2])

    return differences_table


def cubic_spline_interpolation(x_values, y_values):
    n = len(x_values)
    h = [x_values[i + 1] - x_values[i] for i in range(n - 1)]

    A = np.zeros((n, n))
    A[0, 0] = 1
    A[n - 1, n - 1] = 1
    for i in range(1, n - 1):
        A[i, i - 1] = h[i - 1]
        A[i, i] = 2 * (h[i - 1] + h[i])
        A[i, i + 1] = h[i]

    b = np.zeros(n)
    for i in range(1, n - 1):
        b[i] = 3 * (
            (y_values[i + 1] - y_values[i]) / h[i]
            - (y_values[i] - y_values[i - 1]) / h[i - 1]
        )

    x_result = thomas_algorithm(A, b)

    return A, b, x_result


def thomas_algorithm(A_matrix, b_vector):
    n = len(b_vector)
    c, d = [0] * n, [0] * n
    c[0] = A_matrix[0, 0] / A_matrix[0, 0]
    d[0] = b_vector[0] / A_matrix[0, 0]

    for i in range(1, n):
        c[i] = A_matrix[i, i] - A_matrix[i, i - 1] * A_matrix[i - 1, i] / c[i - 1]
        d[i] = (b_vector[i] - A_matrix[i, i - 1] * d[i - 1]) / c[i]

    x_solution = np.zeros(n)
    x_solution[n - 1] = d[n - 1]
    for i in range(n - 2, -1, -1):
        x_solution[i] = d[i] - A_matrix[i, i + 1] * x_solution[i + 1] / c[i]

    return x_solution


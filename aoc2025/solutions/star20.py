"""Solution for 2025 star 20.

Problem page:
    https://adventofcode.com/2025/day/10

Solutions:
    1. Brute force, backtracking
        - O(m * 2^(n + j) * k) time, O(n + k) auxiliary space,
            where m = number of machines,
                  n = maximum number of buttons on a machine,
                  k = maximum number of indicator lights on a machine,
                  j = maximum sum of joltage requirements of a machine
    2. Gaussian elimination + integer linear programming
        - O(mnk + ?) time, O(mnk + ?) auxiliary space
"""

from fractions import Fraction
import math
from typing import Optional, Union

from scipy.optimize import milp, LinearConstraint

from aoc2025.solutions import star19


Matrix = list[list[Union[Fraction, int]]]


def make_augmented_matrix(buttons: list[int], joltages: list[int]) -> Matrix:
    """Make an augmented matrix representing button effects and joltage requirements."""
    n, k = len(buttons), len(joltages)
    matrix = [[0] * (n + 1) for _ in range(k)]

    for i, button in enumerate(buttons):
        for light in button:
            matrix[light][i] = 1

    for i, jolt in enumerate(joltages):
        matrix[i][-1] = jolt

    return matrix


def forward_elimination(matrix: Matrix) -> list[int]:
    """Transform the given matrix into reduced row echelon form. Return the free variables."""
    rows, cols = len(matrix), len(matrix[0])
    free_variables = []
    row, col = 0, 0

    while row < rows and col < cols - 1:
        # Find the row with the largest absolute value of the current column
        pivot_row = row

        for r in range(row + 1, rows):
            if abs(matrix[r][col]) > abs(matrix[pivot_row][col]):
                pivot_row = r

        # No pivot in this column, move to next column
        if matrix[pivot_row][col] == 0:
            free_variables.append(col)
            col += 1
            continue

        # Swap current row with the pivot row
        matrix[pivot_row], matrix[row] = matrix[row], matrix[pivot_row]

        # Standardize pivot column to one
        if matrix[row][col] != 1:
            factor = simplify_int(Fraction(1, matrix[row][col]))

            for c in range(col, cols):
                matrix[row][c] = simplify_int(factor * matrix[row][c])

        # Eliminate other rows with non-zero values in the current column
        for r in range(rows):
            if r == row or matrix[r][col] == 0:
                continue

            factor = simplify_int(Fraction(matrix[r][col], matrix[row][col]))
            matrix[r][col] = 0

            for c in range(col + 1, cols):
                matrix[r][c] -= simplify_int(factor * matrix[row][c])

        row += 1
        col += 1

    # Remaining columns are also free variables
    for c in range(col, cols - 1):
        free_variables.append(c)

    return free_variables


def simplify_int(x: Union[Fraction, int]) -> Union[Fraction, int]:
    """If x is a Fraction but an integer, reduce it to an int."""
    return int(x) if x.is_integer() else x


def minimize_variables_sum(matrix: Matrix, free_variables: list[int]) -> int:
    """Find the minimum variables sum by trying all valid values of the free variables."""
    values = {var: 0 for var in free_variables}

    # Backtracking
    def backtrack(curr: int) -> Optional[int]:
        if curr == len(free_variables):
            results = back_substitution(matrix, values)
            return sum(results) if results else None

        min_variables_sum = math.inf
        for val in range(0, 41):
            values[free_variables[curr]] = val
            variables_sum = backtrack(curr + 1)

            if variables_sum is not None and variables_sum < min_variables_sum:
                min_variables_sum = variables_sum

        return min_variables_sum

    return backtrack(0)


def back_substitution(matrix: Matrix, free_variables: dict[int, int]) -> list[int]:
    """Perform back substitution to find values of the variables."""
    num_vars, rows = len(matrix[0]) - 1, len(matrix)

    # Initialize variable values list
    results = [0] * num_vars
    for var, value in free_variables.items():
        results[var] = value

    # Back substitution
    for row in range(rows - 1, -1, -1):
        # Find pivot column
        pivot_column = 0

        while pivot_column < num_vars and matrix[row][pivot_column] == 0:
            pivot_column += 1

        # This formula is all zeros, move to next formula
        if pivot_column == num_vars:
            continue

        # Find solution for this variable
        results[pivot_column] = matrix[row][-1]

        for col in range(num_vars - 1, pivot_column, -1):
            results[pivot_column] -= matrix[row][col] * results[col]

        # Non-negative or non-integer solution
        if results[pivot_column] < 0 or not results[pivot_column].is_integer():
            return []

        results[pivot_column] = int(results[pivot_column])

    return results


def solve_with_scipy(matrix: Matrix) -> list[int]:
    """Use SciPy to optimize for fewest total button clicks."""
    rows, num_vars = len(matrix), len(matrix[0]) - 1
    objective, integrality = [1] * num_vars, [1] * num_vars

    coefficients = [[matrix[r][c] for c in range(num_vars)] for r in range(rows)]
    lower_bounds = [matrix[r][-1] for r in range(rows)]
    upper_bounds = lower_bounds.copy()
    constraints = LinearConstraint(coefficients, lower_bounds, upper_bounds)

    result = milp(c=objective, constraints=constraints, integrality=integrality)
    return [round(v) for v in result.x]


def run(manual: list[tuple[str, list[list[int]]]]) -> int:
    """Find the sum of fewest button clicks to configure joltage levels."""
    ans = 0

    for _, configs in manual:
        buttons, joltages = configs[:-1], configs[-1]

        # Perform Gaussian elimination
        matrix = make_augmented_matrix(buttons, joltages)
        ref_ans = sum(solve_with_scipy(matrix))  # Obtain reference answer
        free_variables = forward_elimination(matrix)

        if not free_variables:
            algo_ans = sum(back_substitution(matrix, {}))
        else:
            # Perform linear integer programming if any free variables
            algo_ans = minimize_variables_sum(matrix, free_variables)

        if ref_ans != algo_ans:
            print(f"mismatch: scipy={ref_ans} algo={algo_ans}")

        ans += ref_ans

    return ans


PARSER = star19.PARSER
PRINTER = str

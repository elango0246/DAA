from scipy.optimize import linear_sum_assignment
import numpy as np

def assignment_problem(cost_matrix):
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    return row_ind, col_ind, cost_matrix[row_ind, col_ind].sum()

cost_matrix = np.array([[9, 2, 7, 8],
                        [6, 4, 3, 7],
                        [5, 8, 1, 8],
                        [7, 6, 9, 4]])

row_ind, col_ind, total_cost = assignment_problem(cost_matrix)
print(f"Assignment: {list(zip(row_ind, col_ind))}")
print(f"Total Cost: {total_cost}")

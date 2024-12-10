from scipy.optimize import linprog

c = [-1, -2]  # Coefficients for the objective function
A = [[1, 1], [3, 2]]
b = [4, 12]
bounds = [(0, None), (0, None)]

result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
print(result)

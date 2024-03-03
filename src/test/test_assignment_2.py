from ..main import assignment_2
import numpy as np

w = 3.7
degree = 2
xArray = [3.6, 3.8, 3.9]
fxArray = [1.675, 1.436, 1.318]
answer1 = assignment_2.neville_interpolation(w, xArray, fxArray, degree)
print(answer1)
print("\n")


x = [7.2, 7.4, 7.5, 7.6]
y = [23.5492, 25.3913, 26.8224, 27.4589]

diffs = assignment_2.newton_forward_differences(x, y)
result = assignment_2.newton_interpolation(x, y, 7.3, 3, diffs)
for i in range(1, 4):
    print(diffs[i][i])

print("\n")
print(result)
print("\n")

hx = [2.1, 2.5, 2.6]
hy = [5.456, 6.298, 6.427]
hprime = [0.862, 1.489, 1.743]

htable = assignment_2.hermite_differences_table(hx, hy, hprime)

original_print_options = np.get_printoptions()
np.set_printoptions(formatter={"float": "{:0.3e}".format})

for row in htable:
    print(row)

print("\n")
np.set_printoptions(**original_print_options)

xArray = [2, 5, 8, 10]
fxArray = [3, 5, 7, 9]
A, b, x = assignment_2.cubic_spline_interpolation(xArray, fxArray)
print(A)
print(b)
print(x)


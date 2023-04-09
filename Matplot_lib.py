import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(50)
y = np.random.randn(50)
plt.scatter(x, y, facecolor="none", edgecolor="b")
plt.xlabel("x")
plt.ylabel("y")
plt.show()


math_marsk = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.scatter(marks_range, math_marsk, label="math_marsk", color="r")
plt.scatter(marks_range, science_marks, label="science_marks", color="g")
plt.legend()
plt.show()


a = np.array([1, 2, 3])
b = np.array([2, 3, 5])
x = np.arange(1, 11)
y = x * x
plt.title("line graph")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x, y, color="r")
plt.show()

import matplotlib.pyplot as plt
import MyTest
# sample points
X = [0, 5, 10, 15, 20]
Y = [0, 7, 10, 13, 20]
U = MyTest.do_x_data(MyTest.ITER)
V = MyTest.do_profile()


# solve for a and b
def best_fit(X, Y):
    xbar = sum(X)/len(X)
    ybar = sum(Y)/len(Y)
    n = len(X)
    numer = sum([xi*yi for xi,yi in zip(X, Y)]) - n * xbar * ybar
    denum = sum([xi**2 for xi in X]) - n * xbar**2
    b = numer / denum
    a = ybar - b * xbar
    print('best fit line:\ny = {:.2f} + {:.2f}x'.format(a, b))
    return a, b


# solution
a, b = best_fit(U, V)
vfit = [a + b * xi for xi in U]
plt.plot(U, vfit)
# points and graphic shows
plt.plot(U, V)
plt.show()

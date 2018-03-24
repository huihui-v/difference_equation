import numpy as np

# trapezoid method in numerical integration
def trapezoid(f, left, right):
    return (f(left)+f(right))*(right-left)/2

# Rectangle method in numerical integration
def rectangle(f, a, b, N=50):
    x = np.linspace(a, b, N)
    fx = np.zeros((N, 1))
    for i in range(1, x.size):
        fx[i-1] = f(x[i])
    area = np.sum(fx)*((b-a)/N)
    return area
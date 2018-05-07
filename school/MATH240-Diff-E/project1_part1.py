from prettytable import PrettyTable
from matplotlib import pyplot as plt
import numpy as np

def derivative(x, y, counter=None):
    # Calculate the derivative given x, y
    return np.sin(x)*(1-y)

def func(x, y=None):
    # Calculate the "actual" values if we have a solution of the ODE
    return 1 + (y_0 - 1)*np.power(np.e, (np.cos(x) - 1))

def euler(x_arr, y_arr, h):
    """Regular Euler method.  Return array with y values."""
    # Start at array element 1 since 0 is given as initial conditions.
    # Stop before the next-to-last element since we compute y[next]
    # each iteration of the loop.
    for n, x_n in enumerate(x_arr[:-1]):
        y_n = y_arr[n]
        y_arr[n + 1] = y_n + h * derivative(x_n, y_n)
    return y_arr

def euler_improved(x_arr, y_arr, h):
    """Improved Euler method.  Return array with y values."""
    for n, x_n in enumerate(x_arr[:-1]):
        y_n = y_arr[n]
        y_nsplat = y_n + h * derivative(x_n, y_n)
        y_arr[n + 1] = y_n + h * (derivative(x_n, y_n) + derivative(x_n + h, y_nsplat)) / 2
    return y_arr
        
def rk4(x_arr, y_arr, h):
    """RK4 method.  Return array with y values."""
    for n, x_n in enumerate(x_arr[:-1]):
        y_n = y_arr[n]
        k1 = derivative(x_n, y_n)
        k2 = derivative(x_n + h / 2, y_n + h / 2 * k1)
        k3 = derivative(x_n + h / 2, y_n + h / 2 * k2)
        k4 = derivative(x_n + h, y_n + h * k3)
        y_arr[n + 1] = y_n + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return y_arr

def make_table(x_arr, y_arr, prec, i):
    """Generate a human-friendly table based on a pair (x,y) of arrays."""
    tbl = PrettyTable()
    tbl.field_names = ["x_n", "y_n", "n", "Actual", "Abs. error", "%Rel. error"]
    tbl.float_format=prec
    actual = func(x_arr, y_arr)
    abs_err = np.absolute(actual - y_arr)
    rel_err = (abs_err / np.absolute(actual)) * 100
    for n, (x_n, y_n) in enumerate(zip(x_arr, y_arr)):
        tbl.add_row([x_n, y_n, n, actual[n], abs_err[n], rel_err[n]])
    print(tbl)

    #plt.figure(i)
    fig = plt.figure(figsize=(8,6))
    ax1 = fig.add_subplot(211)
    ax1.plot(x_arr, y_arr, color="blue")
    ax1.plot(x_arr, actual, color="green")
    plt.setp(ax1.get_xticklabels(), visible=False)
    ax2 = fig.add_subplot(212, sharex=ax1)
    ax2.set_title("Absolute Error")
    ax2.semilogy(x_arr, abs_err)
    plt.show()

# Initial conditions.
y_0 = -1/2
x_0 = 0
h = 1/16
target = 20
x_n = np.arange(x_0, target, h)

for i, f in enumerate([euler, euler_improved, rk4]):
    # Allocate memory for array, fill with zeros
    y_n = np.zeros(x_n.shape[0])
    # Set only known value
    y_n[0] = y_0
    y_returned = f(x_n, y_n, h)
    prec = "1.4" if f != rk4 else "1.8"
    make_table(x_n, y_returned, prec, i)
    # force cleanup
    del y_n
    del y_returned
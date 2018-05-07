from prettytable import PrettyTable
from matplotlib import pyplot as plt
import numpy as np

def derivative(x, y, counter=None):
    # Calculate the derivative given x, y
    return y - (y * y) + 1.14 * np.cos(np.exp(x/2))

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
    tbl.field_names = ["x_n", "y_n", "n"]
    tbl.float_format=prec
    filt_y = y_arr[np.where(abs(y_arr) < 1000)]
    filt_x = x_arr[0:filt_y.shape[0]]
    for n, (x_n, y_n) in enumerate(zip(filt_x, filt_y)):
        tbl.add_row([x_n, y_n, n])
    print(tbl)

    #plt.figure(i)
    fig = plt.figure(figsize=(8,6))
    plt.plot(filt_x, filt_y, color="blue")
    plt.show()

# Initial conditions.
y_0 = 1
x_0 = 0
h_list = [1/8, 1/16, 1/32, 1/64]
target = 20

# Part 2
print("Improved Euler")
for i, h in enumerate(h_list):
    print("h = %d/%d" % (h.as_integer_ratio()))
    x_n = np.arange(x_0, target, h, dtype=np.float64)
    # Allocate memory for array, fill with zeros
    y_n = np.zeros(x_n.shape[0], dtype=np.float64)
    # Set only known value
    y_n[0] = y_0
    y_returned = euler_improved(x_n, y_n, h)
    prec = "1.4"
    make_table(x_n, y_returned, prec, i)
    # force cleanup
    del y_n
    del y_returned

# Part 2B
# print("\n\n\n")

# print("RK4")
# for i, h in enumerate(h_list):
#     print("h = %d/%d" % (h.as_integer_ratio()))
#     x_n = np.arange(x_0, target, h, dtype=np.float64)
#     # Allocate memory for array, fill with zeros
#     y_n = np.zeros(x_n.shape[0], dtype=np.float64)
#     # Set only known value
#     y_n[0] = y_0
#     y_returned = rk4(x_n, y_n, h)
#     prec = "1.4"
#     make_table(x_n, y_returned, prec, i)
#     # force cleanup
#     del y_n
#     del y_returned
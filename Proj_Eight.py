# Connor Bennett
# 02_2023

import math
import random
import matplotlib.pyplot as plt


def test2(x):
    return 1.0 / 3.0 * x ** 3


def test3(x):
    return math.sin(x) + 1.0


def integrate(f, a, b, n):
    """
    the function to integrate
    the lower limit a
    the upper limit b
    the number of intervals n
    return the value of the integration
    """
    # using trapezoid rule
    t = f(a) + f(b)
    dx = float(b - a) / float(n)
    for i in range(1, n):
        x = a + i * dx
        t = t + 2 * f(x)
    t = t * dx / 2.0
    return t


def random3x2():
    """
    takes no parameters and returns one random number from this distribution.
    Use the python function random.random() to generate a uniform random number [0,1].
    Use a loop to call your random3xsq function 1 million times and then use your histogram
    function to plot a histogram of the values.  Use the parameters density=True, y_label=”probability”, bin_w=.01, bin_start=0
    :return: r
    """
    u = random.random()
    r = u ** (1 / 3)
    return r


def hist(ax, values, x_label, title='', y_label='Frequency',
         density=False, bin_w=0, bin_start=0.0):
    """
    Plots a hist by frequency or density
    :param ax:
    :param values:
    :param x_label:
    :param title:
    :param y_label:
    :param density:
    :param bin_w:
    :param bin_start:
    :return:hist
    """
    m = max(values)
    if (bin_w == 0):
        # no binning
        h = [0] * (m + 1)
        for x in values:
            h[x] += 1
    else:
        nbins = int((m - bin_start) / bin_w + 1)  # number of bins
        h = [0] * nbins
        x_axis = [0] * nbins
        for i in range(nbins):
            x_axis[i] = bin_start + bin_w * i
        for x in values:
            ibin = int((x - bin_start) / bin_w)
            h[ibin] += 1

    if (density):
        for i in range(len(h)):
            h[i] = h[i] / len(values)
    # the histogram of the data
    if (bin_w == 0):
        ax.bar(range(m + 1), h, width=1, align='center')
    else:
        ax.bar(x_axis, h, width=bin_w, align='edge')
    # the x and y axis labels and title
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    if len(title) > 0:
        ax.set_title(title)


def runtest(f, a, b, correct):
    n = 1
    ans = 0.0
    while (abs(ans - correct) > .01):
        n = n * 2
        ans = integrate(f, a, b, n)
        print('n=%d ans=%.3f' % (n, ans))


# main program
# part 1
print("test1 f(x)=sin(x), 0,pi")
runtest(math.sin, 0, math.pi, 2.0)

print("test2 f(x)=1/3*x**3, from 1 to 4")
runtest(test2, 1, 4, 21.25)

print("test3 f(x)=sin(x)+1, from 0 to 2pi")
runtest(test3, 0, 2.0 * math.pi, 2.0 * math.pi)

# This will generate 1 million random number and plot histogram
v = []
for i in range(1000000):
    v.append(random3x2())

fig, ax = plt.subplots()
hist(ax, v, 'x',
     title="random value from distribution with pdf(x)=3x**2",
     y_label="density",
     density=True,
     bin_w=.01,
     bin_start=0)
# display the chart
plt.show()



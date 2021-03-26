from matplotlib import pyplot
from functools import partial
import timeit

def plotTC(fn, nMin, nMax, nInc, nTests):
    # Plot the complexity of our algorithm
    x = []
    y = []
    for i in range(nMin, nMax, nInc):
        print(i)
        N = i
        testNTimer = timeit.Timer(partial(fn, N))
        t = testNTimer.timeit(number=nTests)
        x.append(i)
        y.append(t)
    p1 = pyplot.plot(x, y, 'o')

def algorithmTest(N):
    # A simplified version of our algorithm, runs through the primary steps it takes
    for i in range(N):
        for j in range(N):
            if (j+1 < N):
                for k in range(1):
                    # Simulate the constant number of genres we have
                    # a = i*j just gives the algorithm something to do
                    a=i*j

def n2Algorithm(N):
    # A simple n^2 algorithm
    for i in range(N):
        for j in range(N):
            a=i*j

def n3Algorithm(N):
    # A simple n^3 algorithm
    for i in range(N):
        for j in range(N):
            for k in range(N):
                a=i*j

plotTC( algorithmTest, 10, 200, 2, 10)
plotTC( n2Algorithm, 10, 200, 2, 10)
#plotTC( n3Algorithm, 10, 100, 1, 10)
pyplot.show()
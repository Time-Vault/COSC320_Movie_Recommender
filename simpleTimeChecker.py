from matplotlib import pyplot
from functools import partial
import timeit

def plotTC(nMin, nMax, nInc, nTests):
    # Plot the complexity of our algorithm
    x = []
    y = []
    for i in range(nMin, nMax, nInc):
        print(i)
        N = i
        testNTimer = timeit.Timer(partial(algorithmTest, N))
        t = testNTimer.timeit(number=nTests)
        x.append(i)
        y.append(t)
    p1 = pyplot.plot(x, y, 'o')

def algorithmTest(N):
    # A simplified version of our algorithm, runs through the primary steps it takes
    for i in range(N):
        for j in range(N):
            if (j+1 < N):
                for k in range(10):
                    # Simulate the constant number of genres we have
                    # a = i*j just gives the algorithm something to do
                    a=i*j

plotTC(10, 1000, 10, 10)
pyplot.show()
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

def similarityAlgorithmTest(N):
    # A simplified version of our algorithm, runs through the primary steps it takes
    for i in range(N):
        for j in range(N):
            if (j+1 < N):
                for k in range(1):
                    # Simulate the constant number of genres we have
                    # a = i*j just gives the algorithm something to do
                    a=i*j

def recommenderAlgorithmTest(N):
    # A simplified version of our algorithm, runs through the primary steps it takes
    a = []
    for i in range(N):
        for j in range(N):
            if (j +1 < N & j != i):
                for k in range(5):
                    for p in range(5):
                        if (i%2==0):
                            # Add the 'movie' to the array
                            a.append(i)


def nAlgorithm(N):
    # A simple n^2 algorithm
    for i in range(N):
        a=i*i

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
                a=i*j*k

def n4Algorithm(N):
    # A simple n^3 algorithm
    for i in range(N):
        for j in range(N):
            for k in range(N):
                for h in range(N):
                    a=i*j*k*h

def n5Algorithm(N):
    # A simple n^5 algorithm
    for i in range(N):
        for j in range(N):
            for k in range(N):
                for h in range(N):
                    for f in range(N):
                        a=i*j*k*h*f

def nlognAlgorithm(N):
    a = []
    for i in range(N):
        a.append(i)
    for i in range(N):
        nlognHelper(a, i)
    
def nlognHelper(data, value):
    n = len(data)
    left = 0
    right = n - 1
    while left <= right:
        middle = (left + right) // 2
        if value < data[middle]:
            right = middle - 1
        elif value > data[middle]:
            left = middle + 1
        else:
            return middle


plotTC( recommenderAlgorithmTest, 10, 100, 1, 10)
#plotTC( similarityAlgorithmTest, 10, 200, 2, 10)
#plotTC( nAlgorithm, 10, 200, 2, 10)
#plotTC( nlognAlgorithm, 10, 200, 2, 10)
plotTC( n2Algorithm, 10, 100, 1, 10)
#plotTC( n4Algorithm, 10, 50, 1, 10)
#plotTC( n3Algorithm, 10, 50, 1, 10)
pyplot.show()
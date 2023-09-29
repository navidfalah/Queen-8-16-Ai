import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np


def FitEvolution(meanFit):
    plt.plot(meanFit)
    plt.grid()
    plt.title("Evolution of Fitting")
    plt.ylabel("Fit Mean")
    plt.xlabel("Generation")
    plt.show()

def ShowCheckBoard(solution):
   
    def checkerboard(shape):
        return np.indices(shape).sum(axis=0) % 2

    sol = solution - 1
    size = len(sol)
    color = 0.5
    board = checkerboard((size, size)).astype('float64')
    for i in range(size):
        board[i, int(sol[i])] = color

    fig, ax = plt.subplots()
    ax.imshow(board, cmap=plt.cm.CMRmap, interpolation='nearest')
    plt.show()

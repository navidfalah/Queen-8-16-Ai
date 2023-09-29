import numpy as np
import random
from genetics import(
    Checkfitness, Crossover,
    Selection, Swape
)
from plotter import(
    FitEvolution, ShowCheckBoard
)
from constants import(
    npop, size, ox_size,
    generation, p_sel,
    p_m, numberOfSwaps
)


pop = np.zeros((npop, size), dtype=int)
for i in range(npop):
    pop[i, :] = np.random.permutation(size) + 1
fit = Checkfitness(pop)
pop = np.hstack((pop, fit))
meanFit = np.zeros(generation)

for gen in range(generation):
    print(f"Generation: {gen} / {generation}")
    parents = [Selection(pop, p_sel), Selection(pop, p_sel)]
    offsprings = Crossover(parents[0][0:size], parents[1][0:size], ox_size)

    for i in range(len(offsprings)):
        r_m = round(random.random(), 2)
        if r_m <= p_m:
            offsprings[i] = Swape(offsprings[i], num_swaps=numberOfSwaps) 

    fit_offsprings = Checkfitness(offsprings)
    offsprings = np.hstack((offsprings, fit_offsprings))
    pop = np.vstack([pop, offsprings])
    pop = pop[pop[:, size].argsort()][:npop, :]
    meanFit[gen] = pop[:, size].mean()

#Best solution
bestSol = pop[np.argmin(pop[:, size]), :]

# we can use this function to see the progress of genetics algorithm
# FitEvolution(meanFit)

# print(f"Best Solution have: { bestSol[size]} Conflict(s)")
ShowCheckBoard(bestSol[0:size])

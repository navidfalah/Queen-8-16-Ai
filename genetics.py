import numpy as np


def Checkfitness(population):
    fit = np.zeros((population.shape[0], 1))
    for i, solution in enumerate(population):
        for j in range(len(solution)):
            for k in range(j+1, len(solution)):
                if abs(solution[j] - solution[k]) == abs(j - k):
                    fit[i] += 1
    return fit

def Crossover(parent1, parent2, size):
    
    def fill_gene(f, p):
        unfilled_indices = np.where(f == 0)[0]
        missing_values = np.setdiff1d(p, f)
        f[unfilled_indices[:len(missing_values)]] = missing_values
        return f

    offspring1 = np.zeros(len(parent1), dtype=int)
    offspring2 = np.zeros(len(parent2), dtype=int)

    crossover_point = np.random.randint(0, len(parent1) - size)
    offspring1[crossover_point:crossover_point+size] = parent1[crossover_point:crossover_point+size]
    offspring2[crossover_point:crossover_point+size] = parent2[crossover_point:crossover_point+size]

    offspring1 = fill_gene(offspring1, parent2)
    offspring2 = fill_gene(offspring2, parent1)

    return np.concatenate((offspring1[np.newaxis, :], offspring2[np.newaxis, :]), axis=0)

def Selection(population, p_sel):
    selection_size = int(round(population.shape[0] * p_sel))
    selection_indices = np.random.permutation(population.shape[0])[:selection_size]
    best_solution = population[selection_indices[0], :]
    for i in range(1, selection_size):
        if population[selection_indices[i], -1] < best_solution[-1]:
            best_solution = population[selection_indices[i], :]

    return best_solution

def Swape(child, num_swaps):
    for i in range(num_swaps):
        swap_indices = np.random.choice(len(child), 2, replace=False)
        a, b = child[swap_indices[0]], child[swap_indices[1]]
        child[swap_indices[0]], child[swap_indices[1]] = b, a
    return child

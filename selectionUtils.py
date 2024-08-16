#####################################################################################
#                           SelectionUtils file                                     #
# Contains utilities for recombination, parent selection, and survivor selection.   #
#####################################################################################

# imports
import random
from individual import individual
from worldspace import world
from constants import population_size

# fitness function returns a simulate GRT loss for the given path. Note that our objective is to minimize GRT loss,
# so this is a minimization problem where low fitness is a higher number.
def fitness(candidate):
    tot_loss = 0
    for month in candidate.sched:
        for square in candidate.path:
            tot_loss += world[square].encounterProb[month] * candidate.el

    return tot_loss

# 2 parents are always selected. Parent selection is done by MPS.
def parent_selection(population):
    # determine total fitness of population
    tot_fitness = 0
    for ind in population:
        tot_fitness += fitness(ind)

    # determine probability distribution of parent selection
    probs = []
    for ind in population:
        p = (1 - (fitness(ind)/tot_fitness))/(len(population) - 1)
        probs.append(p)

    # select first parent
    par = random.random()

    for i in range(len(probs)):
        if par < probs[i]:
            parent_index = i
            break

        par -= probs[i]

    # select second parent
    parent2_index = parent_index

    # we don't want to choose the same parent twice!
    counter = 0
    while parent2_index == parent_index:
        par = random.random()

        for i in range(len(probs)):
            if par < probs[i]:
                parent2_index = i
                break

            par -= probs[i]

        counter += 1
        if counter > 100000:
            pass

    return population[parent_index], population[parent2_index]


# survivor selection is done off of a mu + lambda model, where the top pop-size individuals make up the next population
# after recombination + mutation. Returns the first population_size individuals in a combined previous and current generation
def survivor_selection(comb_pop):
    # ensure fitnesses are up to date
    for ind in comb_pop:
        ind.fitness = fitness(ind)

    comb_pop.sort(key=lambda x: x.el)
    return comb_pop[:population_size]

def recombination(parent1, parent2):
    def coincidence():
        for i in range(1, len(parent1.path) - 1):
            for j in range(1, len(parent2.path) - 1):
                if parent1.path[i] == parent2.path[j]:
                    return (i, j)

        return None

    coindices = coincidence()
    if coindices is not None:
        offspring1 = individual([], parent1.sched, parent1.el)
        offspring2 = individual([], parent2.sched, parent2.el)
        offspring1.path = parent1.path[:coindices[0]] + parent2.path[coindices[1]:]
        offspring2.path = parent2.path[:coindices[1]] + parent1.path[coindices[0]:]
        offspring1.length = len(offspring1.path) * 480
        offspring2.length = len(offspring2.path) * 480
        offspring1.fitness = fitness(offspring1)
        offspring2.fitness = fitness(offspring2)
        return offspring1, offspring2
    else:
        return parent1, parent2
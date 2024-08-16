#############################################################################
#               Main File for Final Project                                 #
#                   Bennet Montgomery                                       #
# Contains the main program loop. This is a parallel processing program.    #
#############################################################################


#imports
from constants import hx_sched, hx_loss, hg_sched, hg_loss, sl_sched, sl_loss, max_path, population_size, \
    num_generations, p_recomb, p_mut
from individual import individual
from selectionUtils import recombination, fitness, parent_selection, survivor_selection
from worldspace import world
import random
import multiprocessing
from copy import copy

# simulator function calculates semi-historical routes with Djikstra's algorithm.
def simulate_convs(convoy_id):
    # find semi-historical routes via DFS. Note: historical strategy is to take the geographically shortest
    # route between the start and goal
    unvisited = world.copy()
    distances = world.copy()
    previous = world.copy()
    for key in distances:
        distances[key] = 1000000000
        previous[key] = None

    root = ''
    sched = None

    if convoy_id == 'HX':
        distances['BB'] = 0
        root = 'BB'
        sched = hx_sched
        loss = hx_loss
    elif convoy_id == 'SL':
        distances['ET'] = 0
        root = 'ET'
        sched = sl_sched
        loss = sl_loss
    elif convoy_id == 'HG':
        distances['CG'] = 0
        root = 'CG'
        sched = hg_sched
        loss = hg_loss
    else:
        raise Exception

    current = root

    while 'AM' in unvisited.keys() and 'AN' in unvisited.keys():
        min_dist = 1000000000
        min_unvisited = None
        for node in unvisited.keys():
            if distances[node] < min_dist:
                min_dist = distances[node]
                min_unvisited = node

        current = min_unvisited

        if current == 'AM' or current == 'AN':
            break

        del unvisited[current]

        for node in world[current].adjacency:
            new_dist = distances[current] + 1
            if new_dist < distances[node]:
                distances[node] = new_dist
                previous[node] = current

    path = []
    current = 'AM' if previous['AM'] is not None else 'AN'
    while current is not None:
        path = [current] + path
        current = previous[current]

    # calculate route performance
    tot = 0
    for month in sched:
        for square in path:
            tot += world[square].encounterProb[month] * loss

    return tot, path

# initialize generates a starting convoy population according to passed parameters. Popsize is the convoy population
# to generate, conv_sched is the departure times of this convoy class by month, conv_loss is the expected loss in
# GRT per U-Boat encounter for this convoy class, and conv_start is the initial node of this convoy
def initialize(popsize, conv_sched, conv_loss, conv_start):
    # initialize population
    population = []
    while len(population) is not popsize:
        # each candidate starts in home node
        candidate = [conv_start]
        # conduct blind search to british nodes
        attempts = 0
        next_node = conv_start
        while attempts < 100:
            # select next node
            next_node = world[next_node].adjacency[random.randrange(len(world[next_node].adjacency))]

            # don't allow doubling back
            if next_node in candidate:
                next_node = candidate[-1]
                attempts += 1
            else:
                # retry if we've mutated to a path beyond the maximum convoy length
                if (len(candidate)+1) * 480 > max_path:
                     candidate = [conv_start]
                     next_node = conv_start
                # exit if we've arrived in Great Britain
                elif world[next_node].inUK:
                    candidate.append(next_node)
                    population.append(individual(candidate, conv_sched, conv_loss))
                    population[-1].fitness = fitness(population[-1])
                    break
                else:
                    candidate.append(next_node)


    return population

# convoyprocess performs generation steps in accordance with GA outline. This is given its own function
def convoyprocess(population):
    num_gens = 0
    best = copy(population[0])

    # iterate through each generation
    while num_gens < num_generations:
        # find best convoy in present generation for this convoy id and find the average fitness in this generation
        tot_fit = 0
        for ind in population:
            # less than because this is a minimization problem
            ind_fit = fitness(ind)
            tot_fit += ind_fit
            if ind_fit < fitness(best):
                best = copy(ind)

        # create a new generation of candidates
        temp_next_gen = []
        while len(temp_next_gen) < population_size:
            parent1, parent2 = parent_selection(population)
            if random.random() < p_recomb:
                offspring1, offspring2 = recombination(parent1, parent2)
            else:
                offspring1, offspring2 = parent1, parent2

            temp_next_gen.append(offspring1)
            temp_next_gen.append(offspring2)

        # potentially apply mutation to ALL members of new generation
        for i in range(population_size):
            if random.random() < p_mut:
                temp_next_gen[i].mutate()

        # select next generation by mu + lambda
        population = survivor_selection(population + temp_next_gen)
        num_gens += 1
        if num_gens % 5 == 0:
            if population[0].path[0] == "BB":
                print("Convoy HX in generation: " + str(num_gens))
                print("Best convoy HX fitness in generation " + str(num_gens) + ": " + str(fitness(best)))
                print("Average convoy HX fitness in generation " + str(num_gens) + ": " + str(tot_fit/population_size))
            elif population[0].path[0] == "ET":
                print("Convoy SL in generation: " + str(num_gens))
                print("Best convoy SL fitness in generation " + str(num_gens) + ": " + str(fitness(best)))
                print("Average convoy SL fitness in generation " + str(num_gens) + ": " + str(tot_fit/population_size))
            elif population[0].path[0] == "CG":
                print("Convoy HG in generation: " + str(num_gens))
                print("Best convoy HG fitness in generation " + str(num_gens) + ": " + str(fitness(best)))
                print("Average convoy HG fitness in generation " + str(num_gens) + ": " + str(tot_fit/population_size))
            else:
                raise Exception

    return best

# main function
def main():
    # apply djikstra's algorithm for semi-historical comparison
    loss, path = simulate_convs('HX')
    print("Semi-Historical route with Djiktra's algorithm GRT loss for Convoy HX: " + str(loss))
    print("Semi-Historical route with Djikstra's algorithm for Convoy HX: " + str(path))
    loss, path = simulate_convs('SL')
    print("Semi-Historical route with Djiktra's algorithm GRT loss for Convoy SL: " + str(loss))
    print("Semi-Historical route with Djikstra's algorithm for Convoy SL: " + str(path))
    loss, path = simulate_convs('HG')
    print("Semi-Historical route with Djiktra's algorithm GRT loss for Convoy HG: " + str(loss))
    print("Semi-Historical route with Djikstra's algorithm for Convoy HG: " + str(path))

    # initialize hx population
    hx = initialize(population_size, hx_sched, hx_loss, "BB")
    # initialize sierra leone population
    sl = initialize(population_size, sl_sched, sl_loss, "ET")
    # initialize gibraltar population
    hg = initialize(population_size, hg_sched, hg_loss, "CG")

    # process in parallel
    pool = multiprocessing.Pool(processes=3)
    results = pool.map(convoyprocess, [hx, sl, hg])

    # display results
    print('Best generated performance for HX (Homeward from Halifax): ' + str(results[0].fitness) + ' GRT lost')
    print('Path is' + str(results[0].path))
    print('Best generated performance for HG (Homeward from Gibraltar): ' + str(results[2].fitness) + ' GRT lost')
    print('Path is' + str(results[2].path))
    print('Best generated performance for SL (Homeward from Sierra Leone): ' + str(results[1].fitness) + ' GRT lost')
    print('Path is' + str(results[1].path))



if __name__ == '__main__':
    main()
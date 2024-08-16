import random
from constants import max_mut_dist, max_path
from worldspace import world

class individual:
    def __init__(self, path, sched, el):
        self.path = path
        self.length = len(path) * 480 # length of this candidate in nautical miles
        self.sched = sched
        self.el = el
        self.fitness = 0 # placeholder

    # mutation application function for individuals
    #   Selects a start and end index and replaces the intermediate path with a new intermediate path
    def mutate(self):
        # fail automatically if path length is too short to mutate
        if len(self.path) < 3:
            return

        # select point to begin mutation
        path_start = random.randrange(len(self.path) - 2) # -2: we don't want to select the last two indices
        highest_path_end = len(self.path) if path_start + int(len(self.path)*max_mut_dist) >= len(self.path) else path_start + int(len(self.path)*max_mut_dist)
        # select point to end mutation
        path_end = random.randrange(start=path_start, stop=max(highest_path_end, path_start+2))

        # replace nodes between points
        new_path = self.path[:path_start+1]
        next_node = self.path[path_start]
        attempt_counter = 0

        while new_path[-1] is not self.path[path_end] and attempt_counter < 100:
            # select random node from adjacencies in world space
            next_node = world[next_node].adjacency[random.randrange(len(world[next_node].adjacency))]

            # reselect if path doubles back
            if next_node in new_path:
                next_node = new_path[-1]
                attempt_counter += 1
            else:
                # exit if we've arrived in Great Britain
                if world[next_node].inUK:
                    new_path.append(next_node)
                    self.path = new_path
                    self.length = len(self.path) * 480
                    return

                # retry if we've mutated to a path beyond the maximum convoy length
                if len(new_path) * 480 + len(self.path[path_end:]) * 480 > max_path or len(new_path) > len(self.path):
                     new_path = self.path[:path_start+1]
                     next_node = self.path[path_start]
                     attempt_counter += 1
                else:
                    new_path.append(next_node)

        if attempt_counter < 100:
            self.path = new_path + self.path[path_end+1:]
            self.length = len(self.path) * 480


    # string display override for individuals
    def __str__(self):
        return 'Path: ' + str(self.path) + '\nPath length: ' + str(self.length)

    # object copy override for individuals, to ensure best solution isn't mutated away
    def __copy__(self):
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__.update(self.__dict__)
        return result
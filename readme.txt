System Requirements:
This program requires parallel processing compatibility with capability of at least 3 parallel processes. This shouldn't
be a problem on any modern machine.

This program contains 6 program files

1. main.py
Contains the main GA execution. This file is divided into 5 functions. simulate_convs applies djikstra's algorithm
to find the shortest route in nautical miles between a given convoy class' starting grid space and the UK and returns
a simulated shipping loss along this route. initialize constructs a population of individuals with random valid candidate
paths for a given convoy class. convoyprocess contains the main GA loop. This is kept separate from main() to allow
for parallel processing. The final function is the program entry point, main.

2. worldspace.py
Contains statistics on each grid square in the relevant area of the Atlantic ocean. Each square contains adjacency data
on squares that can be moved into from it as well as the probability of a U-Boat encounter in this square for a convoy
passing through in a given month (calculated from historical data). This file also contains a world dictionary allowing
quick reference of grid squares.

3. gridSquare.py
Contains the grid square representation class for the German Naval Grid System. Used by worldspace.py

4. individual.py
Contains the individual representation class. Each individual is a path across the Atlantic for a specific convoy class
(HX, HG, or SL). Individuals contain a copy() override, a str() override, and a function for applying mutation to the
route.

5. selectionUtils.py
Contains recombination, fitness, and parent selection functions. Fitness is measured as the total estimated GRT loss
for a candidate solution over all trips made by the solution's convoy class in the [06/1940, 06/1941] period. Parent
selection is done by MPS.

6. constants.py
This contains constants needed across multiple program files. This is its own file to avoid circular imports.
class grid_square:
    def __init__(self, adjacency, encounterProb=[0,0,0,0,0,0,0,0,0,0,0,0,0], inUK=False):
        self.adjacency = adjacency          # matrix of connected tiles
        self.encounterProb = encounterProb  # matrix of probability of encountering a U-Boat here by month
        self.inUK = inUK                    # whether or not this is a destination node for materiel
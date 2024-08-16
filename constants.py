#########################################################################################################
#                                               Constants file                                          #
# Contains GA constants needed by other files. Included in a special file to avoid circular imports.    #
#########################################################################################################
# GA utility constants. P_mut = mutation probability, p_recomb = recombination probability
# max_mut_dist defines how much of a convoy route can be replaced in a mutation operation
# max_path defines the maximum distance, in nautical miles, a route can take
p_mut = 0.05
p_recomb = 0.8
max_mut_dist = 0.5
max_path = 6500
population_size = 100
num_generations = 200
# convoy schedules.
#   Months are in order from June 1940 as 0 to June 1941 as 12
hx_sched = [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5,
            5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 11, 11,
            11, 11, 11, 11, 11, 12, 12, 12]

hg_sched = [0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 6, 7, 7, 7, 8, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12,
            12]

sl_sched = [0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7,
            7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12]

# expected loss from a U-Boat encounter. Based on available U-Boat encounter data for this convoy. Hx had unusually low
# expected loss due to his escort count and surface speed.
hx_loss = 5744
hg_loss = 8000
sl_loss = 8800

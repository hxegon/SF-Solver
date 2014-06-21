from score import Score
from grid import Grid
from finder import Finder
import random

def scores_for(puzzle):
    puzzle = normalize_nums(puzzle)
    F = Finder(Grid(puzzle))
    return sorted([ (Score.calculate_from(F.graph.path_values(path)), path) for path in F.find_all_paths() ])

def new_puzzle():
    return [ random.choice(range(1, 10)) for i in range(0,16) ]

def normalize_nums(num_string):
    return [ int(i) for i in list(num_string) ]

from score import Score
from grid import Grid
from finder import Finder
import random

def scores_for(puzzle):
    F = Finder(Grid(puzzle))
    return sorted([ (Score.calculate_from(F.graph.path_values(path)), path) for path in F.find_all_paths() ])
    #scores = [ (Score.calculate_from(F.graph.path_values(path)), path) for path in F.find_all_paths() ]
    #return scores

def new_puzzle():
    return [ random.choice(range(1, 10)) for i in range(0,16) ]

def normalize(num_string):
    pass

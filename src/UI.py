from score import Score
from grid import Grid
from finder import Finder

def scores_for(puzzle):
    F = Finder(Grid(puzzle))
    return sorted([ (Score.calculate_from(F.graph.path_values(path)), path) for path in F.find_all_paths() ])
    scores = [ (Score.calculate_from(F.graph.path_values(path)), path) for path in F.find_all_paths() ]
    #return scores

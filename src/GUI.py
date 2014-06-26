#import sys
from interface import *
import tkinter as tk

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.PuzzleEntryLabel = tk.Label(self.parent, text="Enter Puzzle Numbers Here")
        self.PuzzleEntryLabel.pack()
        
        self.PuzzleEntryBox = tk.Entry(self.parent, textvariable="NewPuzzle")
        self.PuzzleEntryBox.pack()

        self.PuzzleEntryButton = tk.Button(self.parent, text="Enter Puzzle", command=self.EnterPuzzle)
        self.PuzzleEntryButton.pack()


    def EnterPuzzle(self, current_path=-1):
        puzzle = self.PuzzleEntryBox.get()
        if len(puzzle) != 16:
            LabelText = "Incorrect length. string was %s characters, when it needs to be 16 characters" % (len(puzzle))
        else:
            self.scores = scores_for(puzzle) # for use in next/prev
            self.current_path = current_path # for use in next/prev
            ScoreText = str(self.scores[self.current_path][0])
            PathText = self.ShowPath(self.scores[self.current_path][1])
            LabelText = "High Score: %s, Score Path: %s" % (ScoreText, PathText)
        self.PuzzleLabel = tk.Label(self.parent, text=LabelText)
        self.PuzzleLabel.pack()

    # changes a list of lists with (0,1) style grid coords to A2 style grid coords
    def ShowPath(self, path):
        coord_table = { 0: "A", 1: "B", 2: "C", 3: "D" }
        return " ".join([ coord_table[x] + str(y+1) for x, y in path ])

    # TODO next/previous buttons


if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()

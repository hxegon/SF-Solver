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

    def EnterPuzzle(self):
        puzzle = self.PuzzleEntryBox.get()
        if len(puzzle) == 16:
            scores = scores_for(puzzle)[-1]
            ScoreText = str(scores[-1][0])
            PathText = str(scores[-1][1])
            LabelText = "High Score: %s, Score Path: %s" % (ScoreText, PathText)
        else:
            LabelText = "Incorrect length. string was %s characters, when it needs to be 16 characters" % (len(puzzle))
        self.PuzzleLabel = tk.Label(self.parent, text=LabelText)
        self.PuzzleLabel.pack()

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()

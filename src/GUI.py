from interface import *
import tkinter as tk
import locale

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        locale.setlocale(locale.LC_ALL, 'en_US')
        self.PuzzleEntryLabel = tk.Label(self.parent, text="Enter Puzzle Numbers Here", font=("", 16))
        self.PuzzleEntryLabel.pack()
        
        self.PuzzleEntryBox = tk.Entry(self.parent, textvariable="NewPuzzle", font=('', 16))
        self.PuzzleEntryBox.pack()

        self.PuzzleEntryButton = tk.Button(self.parent, text="Enter Puzzle", command=self.EnterPuzzle, font=('', 16))
        self.PuzzleEntryButton.pack()

        self.RandomButton = tk.Button(self.parent, text="Random", command=self.Randomize, font=('', 16))
        self.RandomButton.pack()

    def Randomize(self):
        self.PuzzleEntryBox.delete(0, "end")
        self.PuzzleEntryBox.insert(0, "".join([ str(i) for i in new_puzzle() ]))

    def EnterPuzzle(self, current_path=-1):
        puzzle = self.PuzzleEntryBox.get()
        if len(puzzle) != 16:
            LabelText = "Incorrect length. string was %s characters, when it needs to be 16 characters" % (len(puzzle))
        else:
            self.scores = scores_for(puzzle) # for use in next/prev
            self.current_path = current_path # for use in next/prev
            ScoreText = self.ScoreWithCommas(self.scores[self.current_path][0])
            PathText = self.ShowPath(self.scores[self.current_path][1])
            CoordText = self.ShowCoordPath(self.scores[self.current_path][2])
            LabelText = "High Score: %s\n Score Path: %s\n Path: %s" % (ScoreText, PathText, CoordText)
            try:
                self.HigherButton.destroy()
                self.LowerButton.destroy()
                self.PuzzleLabel.destroy()
            except: pass
            self.HigherButton = tk.Button(self.parent, text="Higher", command=self.HigherButtonAction, font=('', 16))
            self.HigherButton.pack()
            self.LowerButton = tk.Button(self.parent, text="Lower", command=self.LowerButtonAction, font=('', 16))
            self.LowerButton.pack()
        self.PuzzleLabel = tk.Label(self.parent, text=LabelText, font=("", 16))
        self.PuzzleLabel.pack()

    def ScoreWithCommas(self, score):
        return locale.format("%d", score, grouping=True)

    # changes a list of lists with (0,1) style grid coords to A2 style grid coords
    def ShowCoordPath(self, path):
        coord_table = { 0: "A", 1: "B", 2: "C", 3: "D" }
        return " ".join([ coord_table[x] + str(y+1) for x, y in path ])

    def ShowPath(self, path):
        # show path values
        return " ".join([ str(x) for x in path ])

    def LowerButtonAction(self):
        self.EnterPuzzle(self.current_path - 1)
    
    def HigherButtonAction(self):
        self.EnterPuzzle(self.current_path + 1)

def main():
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=False)
    root.mainloop()

if __name__ == "__main__":
    main()

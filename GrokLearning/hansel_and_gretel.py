class Trail:

    def __init__(self, x=None, y=None, grid=None, steps=None):
        self.x = 0
        self.y = 0
        self.steps = {
            "up": (0, -1),
            "down": (0, 1),
            "right": (1, 0),
            "left": (-1, 0)
        }
        self.grid = []

    def setupGrid(self):
        try:
            size = int(input("Grid size: "))
        except ValueError as e:
            #print(f"{e}: Enter integer values only for grid size")
            print(e)

        else:
            for i in range(size):
                row = []
                for j in range(size):
                    row.append(".")
                self.grid.append(row)
            self.grid[0][0] = "x"

    def printGrid(self):
        for row in self.grid:
            for i in row:
                print(i, end="")
            print()

    def editGrid(self):
        while True:
            try:
                direction = input("Direction: ")
            except KeyError as e:
                print(e)
                break
            else:
                if not direction:
                    break
                else:
                    self.x += self.steps[direction][0]
                    self.y += self.steps[direction][1]
                    self.grid[self.y][self.x] = "x"
                    self.printGrid()


myTrail = Trail()
myTrail.setupGrid()
myTrail.printGrid()
myTrail.editGrid()
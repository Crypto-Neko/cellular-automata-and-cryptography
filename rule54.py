from termcolor import colored

class Automata():
    def __init__(self, length, tiles):
        self.len = length
        self.grid = [0]*length
        self.history = [self.grid]
        for tile in tiles:
            self.grid[tile[0]] = tile[1]

    def update(self):
        updated = []
        state = [self.grid[0]]
        i = 1
        while i < self.len:
            if i != 0 and i != self.len-1:
                state.append((self.grid[i-1], self.grid[i], self.grid[i+1]))
            i+=1
        state.append(self.grid[self.len-1])
        updated.append(self.grid[0])
        i = 0
        while i < self.len:
            if state[i] == (1, 1, 1) or state[i] == (1, 1, 0) or state[i] == (0, 1, 1) or state[i] == (0, 0, 0):
                updated.append(0)
            elif state[i] == (1, 0, 1) or state[i] == (1, 0, 0) or state[i] == (0, 1, 0) or state[i] == (0, 0, 1):
                updated.append(1)
            i+=1
        updated.append(self.grid[self.len-1])

        self.history.append(updated)
        self.grid = updated

    def show(self):
        for row in self.history:
            for element in row:
                if element == 1:
                    print(colored(str(element), 'green'), end=" ")
                elif element == 0:
                    print(colored(str(element), 'red'), end=" ")
            print(" ")



tiles = []
tiles.append((15, 1))
automata = Automata(31, tiles)

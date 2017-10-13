import tkinter
import random
import itertools
import collections
import csv

class Field:
    def __init__(self, n = 64, m = 64):
        self.n = n
        self.m = m
        self.field = [[0 for i in range(n)] for j in range(m)]
        self.field[0] = [1 for i in range(n)]
        self.field[n-1] = [1 for i in range(n)]
        for i in range(m):
            self.field[i][0] = 1
            self.field[i][n-1] = 1

        self.automata_list = []

    def update(self):
        self.field = [[0 for i in range(self.n)] for j in range(self.m)]
        self.field[0] = [1 for i in range(self.n)]
        self.field[self.n - 1] = [1 for i in range(self.n)]
        for i in range(self.m):
            self.field[i][0] = 1
            self.field[i][self.n-1] = 1
        for automaton in self.automata_list:
            self.field[automaton.x][automaton.y] = automaton

    def get_grid_state(self, x, y):
        return self.field[x][y]

class Automaton:
    def __init__(self, x, y, color, field):
        self.x = x
        self.y = y
        self.color = color
        self.field = field
        self.color_dic = {'red': 'green', 'green': 'yellow', 'yellow': 'red'}
        self.rectangle = None

    def action(self):
        dx, dy = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
        grid = self.field.get_grid_state(self.x + dx, self.y + dy)
        if type(grid) == Automaton:
            if grid.color == self.color:
                return
            elif grid.color == self.color_dic[self.color]:
                grid.color = self.color
        else:
            if grid == 0:
                new_automata =  Automaton(self.x + dx, self.y + dy, self.color, self.field)
                new_rectangle = canvas.create_rectangle(10 * (self.x + dx), 10 * (self.y + dy),
                                        10 * (self.x + dx) + 10,
                                        10 * (self.y + dy) + 10,
                                        fill=self.color, tag="automata")
                new_automata.rectangle = new_rectangle
                self.field.field[self.x + dx][self.y + dy] = new_automata
                self.field.automata_list.append(new_automata)


root = tkinter.Tk()
root.title('Automata')
size = 50
density = 10
square_size = 10
canvas = tkinter.Canvas(root, width=square_size*size, height=square_size*size)
canvas.pack()
f = Field(n=size, m=size)
automaton = [Automaton(x, y, random.choice(['red', 'green', 'yellow']), f) for x, y
             in itertools.product(range(1, size-1, density), repeat=2)]
rectangles = [canvas.create_rectangle(square_size*automata.x, square_size*automata.y,
                                      square_size*automata.x + square_size, square_size*automata.y + square_size,
                                      fill=automata.color, tag="automata") for automata in automaton]
f.automata_list = automaton

for rectangle,automata in zip(rectangles, automaton):
    automata.rectangle = rectangle


def move_rectangles(automaton, canvas, f):
    count_dict = collections.Counter(list(map(lambda x: x.color, automaton)))
    l=[count_dict['red'], count_dict['green'], count_dict['yellow']]
    with open('result.csv', 'a') as file:
        writer = csv.writer(file, lineterminator='\n')
        writer.writerow(l)

    for automata in f.automata_list:
        automata.action()
        canvas.itemconfig(automata.rectangle, fill=automata.color)
    f.update()
    root.after(1, move_rectangles, automaton, canvas, f)


root.after(1, move_rectangles, automaton, canvas, f)
root.mainloop()

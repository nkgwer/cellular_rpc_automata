import tkinter
from Bit_monster import *
import itertools
import functools

root = tkinter.Tk()
root.title('bit_monsters')
#root.geometry("640x640")
size = 200
density = 2
square_size = 750//size
canvas = tkinter.Canvas(root, width=square_size*size, height=square_size*size)
canvas.pack()
f = Field(n=size)
monsters = [Bitmonster(x, y, random.choice(['red', 'blue', 'green']), f) for x, y in itertools.product(range(1, size-1, density), repeat=2)]
rectangles = [canvas.create_rectangle(square_size*monster.x, square_size*monster.y, square_size*monster.x + square_size, square_size*monster.y + square_size,
                                      fill=monster.color, tag="monster") for monster in monsters]
f.monsters = monsters


def move_rectangles(rectangles, monsters, canvas, f):
    for rectangle, monster in zip(rectangles, monsters):
        monster.move()
        canvas.coords(rectangle, square_size*monster.x, square_size*monster.y, square_size*monster.x+square_size, square_size*monster.y+square_size)
    f.update()
    root.after(1, move_rectangles, rectangles, monsters, canvas, f)


root.after(1, move_rectangles, rectangles, monsters, canvas, f)
root.mainloop()

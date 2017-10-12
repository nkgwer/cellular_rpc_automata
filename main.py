import tkinter
from Bit_monster import *
import itertools
import functools

root = tkinter.Tk()
root.title('bit_monsters')
#root.geometry("640x640")
size = 64
canvas = tkinter.Canvas(root, width=10*size, height=10*size)
canvas.pack()
f = Field(n=size)
monsters = [Bitmonster(x, y, random.choice(['red', 'blue', 'green', 'yellow']), f) for x, y in itertools.product(range(1, size-1, 2), repeat=2)]
rectangles = [canvas.create_rectangle(10*monster.x, 10*monster.y, 10*monster.x + 10, 10*monster.y + 10,
                                      fill=monster.color, tag="monster") for monster in monsters]
f.monsters = monsters


def move_rectangles(rectangles, monsters, canvas, f):
    for rectangle, monster in zip(rectangles, monsters):
        monster.move()
        canvas.coords(rectangle, 10*monster.x, 10*monster.y, 10*monster.x+10, 10*monster.y+10)
    f.update()
    root.after(1, move_rectangles, rectangles, monsters, canvas, f)


root.after(1, move_rectangles, rectangles, monsters, canvas, f)
root.mainloop()

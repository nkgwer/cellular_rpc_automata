import tkinter
from Bit_monster import *
from time import sleep


root = tkinter.Tk()
root.title('bit_monsters')
root.geometry("640x640")
canvas = tkinter.Canvas(root, width=640, height=640)
canvas.pack()
f = Field(n=64)
monsters = [Bitmonster(random.randint(3,60), random.randint(3,60),random.choice(['red', 'yellow', 'green']), f) for i in range(200)]
rectangles = [canvas.create_rectangle(10*monster.x, 10*monster.y, 10*monster.x + 10, 10*monster.y + 10,
                                      fill=monster.color, tag="monster") for monster in monsters]
f.monsters = monsters

while False:
    for monster in monsters:
        monster.move()

    sleep(1)
    canvas.delete("monster")
    canvas.pack()
    root.update()


def move_rectangles(rectangles, monsters, canvas, f):
    for rectangle, monster in zip(rectangles, monsters):
        monster.move()
        canvas.coords(rectangle, 10*monster.x, 10*monster.y, 10*monster.x+10, 10*monster.y+10)
        f.update()
    root.after(10, move_rectangles, rectangles, monsters, canvas, f)


root.after(10, move_rectangles, rectangles, monsters, canvas, f)
root.mainloop()
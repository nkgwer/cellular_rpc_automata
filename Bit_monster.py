import random
class Field:
    def __init__(self, n = 64):
        self.n = n
        self.field = [[0 for i in range(n)] for j in range(n)]
        # fill edge with True
        self.field[0] = [1 for i in range(n)]
        self.field[n-1] = [1 for i in range(n)]
        for i in range(n):
            self.field[i][0] = 1
            self.field[i][n-1] = 1

        self.monsters = []

    def update(self):
        self.field = [[0 for i in range(self.n)] for j in range(self.n)]
        self.field[0] = [1 for i in range(self.n)]
        self.field[self.n - 1] = [1 for i in range(self.n)]
        for i in range(self.n):
            self.field[i][0] = 1
            self.field[i][self.n-1] = 1
        for monster in self.monsters:
            self.field[monster.x][monster.y] = monster

    def get_grid_state(self, x, y):
        return self.field[x][y]



class Bitmonster:
    def __init__(self, x, y, color, field, name = 'bibi'):
        self.x = x
        self.y = y
        self.color = color
        self.color_dict = {'red': 'green', 'green': 'yellow', 'yellow': 'blue', 'blue': 'red'}
        self.name = name
        self.field = field
        self.direction_dic = {'up': (0, 1), 'right': (1, 0), 'down': (0, -1),'left': (-1, 0)}
        self.direction = random.choice(['up', 'right', 'down', 'left'])
        self.move_dic = {'up': ['right', 'left'], 'right': ['down', 'up'],
                         'down': ['left', 'right'], 'left': ['up', 'down']}

        self.joined = False
        self.length = 0

    def move(self):
        if self.joined:
            return
        patterns = [(0, 1), (1, 0),(-1,0),(0,-1)]
        adj = 0
        for dx, dy in patterns:
            grid = self.field.get_grid_state(self.x+dx, self.y+dy)
            if type(grid) == Bitmonster:
                if grid.color == self.color_dict[self.color]:
                    adj += 1
                else:
                    adj = 0
                    break
            if adj > 1:
                break
        if adj == 1:
            for dx, dy in patterns:
                grid = self.field.get_grid_state(self.x + dx, self.y + dy)
                if type(grid) == Bitmonster:
                    grid.joined = True
            self.joined = True
            return

        if self.field.get_grid_state(self.x + self.direction_dic[self.direction][0],
                                     self.y + self.direction_dic[self.direction][1]) == 0:
            self.x += self.direction_dic[self.direction][0]
            self.y += self.direction_dic[self.direction][1]
        else:
            self.direction = random.choice(self.move_dic[self.direction])






import random
import copy
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


class Block:
    def __init__(self):
        self.member = set()

    def get_len(self):
        return len(self.member)


class Bitmonster:
    def __init__(self, x, y, color, field, name = 'bibi'):
        self.x = x
        self.y = y
        self.color = color
        self.name = name
        self.field = field
        self.direction_dic = {'up': (0, 1), 'right': (1, 0), 'down': (0, -1),'left': (-1, 0)}
        self.direction = random.choice(['up', 'right', 'down', 'left'])
        self.move_dic = {'up': ['right', 'left'], 'right': ['down', 'up'],
                         'down': ['left', 'right'], 'left': ['up', 'down']}
        self.neighbors = set()
        self.longest_ever_seen = 0
        self.block = None


    def move(self):
        #print(self.longest_ever_seen)
        patterns = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        self.neighbors.clear()
        for dx, dy in patterns:
            grid = self.field.get_grid_state(self.x+dx, self.y+dy)
            if type(grid) == Bitmonster:
                self.neighbors.add(grid)

        if self.block:
            #print(self.block.get_len())
            return

        else:
            print(self.longest_ever_seen)
            if len(self.neighbors) > 2:
                for neighbor in self.neighbors:
                    if neighbor.color != self.color:
                        if neighbor.block:
                            if neighbor.block.get_len() >= self.longest_ever_seen:
                                neighbor.block.member.add(self)
                                self.block = neighbor.block
                                return
                        else:
                            if self.longest_ever_seen == 0:
                                self.block = Block()
                                self.block.member.add(self)
                                self.block.member.add(neighbor)
                                neighbor.block = self.block
                                return


            front = self.field.get_grid_state(self.x + self.direction_dic[self.direction][0],
                                              self.y + self.direction_dic[self.direction][1])

            if front == 0:
                self.x += self.direction_dic[self.direction][0]
                self.y += self.direction_dic[self.direction][1]
                return

            elif type(front) == Bitmonster:
                if front.block:
                    if self.longest_ever_seen <= len(front.block.member):
                        self.longest_ever_seen = len(front.block.member)
                    else:
                        for member in front.block.member:
                            member.block = None
                            member.longest_ever_seen = self.longest_ever_seen
                        print("kaisan")
                else:
                    front.longest_ever_seen, self.longest_ever_seen = max(front.longest_ever_seen, self.longest_ever_seen), max(front.longest_ever_seen, self.longest_ever_seen)
                self.direction = random.choice(self.move_dic[self.direction])

            elif front == 1:
                self.direction = random.choice(self.move_dic[self.direction])

            else:
                print('WTF')





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
        self.neighbors = set()
        self.joined_neighbors = set()
        self.longest_ever_seen = 0

    def move(self):
        patterns = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        self.neighbors.clear()
        for dx, dy in patterns:
            grid = self.field.get_grid_state(self.x+dx, self.y+dy)
            if type(grid) == Bitmonster:
                self.neighbors.add(grid)

        if self.joined:
            print(len(self.joined_neighbors))
            for neighbor in self.neighbors:
                if neighbor.joined:
                    self.joined_neighbors.add(neighbor)
                self.joined_neighbors = self.joined_neighbors.union(neighbor.joined_neighbors)
            return

        else:
            self.joined_neighbors.clear()
            for neighbor in self.neighbors:
                if neighbor.color != self.color and len(neighbor.joined_neighbors) >= self.longest_ever_seen:
                    self.joined = True
                    neighbor.joined = True


        front = self.field.get_grid_state(self.x + self.direction_dic[self.direction][0],
                                     self.y + self.direction_dic[self.direction][1])

        if front == 0:
            self.x += self.direction_dic[self.direction][0]
            self.y += self.direction_dic[self.direction][1]
            return

        elif type(front) == Bitmonster:
            if self.longest_ever_seen <= len(front.joined_neighbors):
                self.longest_ever_seen = len(front.joined_neighbors)
            else:
                front.joined = False
                neighbor_of_front = copy.copy(front.joined_neighbors)
                for front_neighbor in neighbor_of_front:
                    front_neighbor.joined = False
                    front_neighbor.longest_ever_seen = self.longest_ever_seen
                    front_neighbor.joined_neighbors.clear()
                print("kaisan")


            #print(self.longest_ever_seen)
            self.direction = random.choice(self.move_dic[self.direction])

        elif front == 1:
            self.direction = random.choice(self.move_dic[self.direction])

        else:
            print('WTF')





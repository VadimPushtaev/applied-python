import random
import solver
import copy
import BaseGame

NAME = "SUDOKU"

class Game(BaseGame.BaseGame):    
    def run(self):
        Wrapper()
        

class Wrapper():
    SET_OF_LETTER = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
    SET_COLUMN = {'1':0,'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,'9':8}

    def __init__(self, name = 'Player 1'):
        self.name = name
        self.points = 0
        self._start_game()
    
    def _start_game(self):
        obj_sudoku = Sudoku()
        print('От игрока требуется заполнить свободные клетки цифрами от 1 до 9 так, '
              'чтобы в каждой строке, в каждом столбце и в каждом малом квадрате 3×3 '
              'каждая цифра встречалась бы только один раз. '
              'Пример ввода: А 1 8')
        print('Игрок: ', self.name)
        while not obj_sudoku.check_game():
            obj_sudoku.pprint()
            obj_sudoku = self.input_element(obj_sudoku)


    def input_element(self, obj):
        position = input()
        position = position.split()
        obj.set_value(self.SET_OF_LETTER.get(position[0]), self.SET_COLUMN.get(position[1]), int(position[2]))
        return obj


class Grid:
    def __init__(self, n=3):
        self.size = n
        self.table = [[((i * n + i // n + j) % (n * n) + 1) for j in range(n * n)] for i in range(n * n)]

    def pprint(self):
        for i in self.table:
            print(i)

    def transporting(self):
        self.table = list(map(list, zip(*self.table)))

    def swap_rows_small(self):
        area = random.randrange(0, self.size, 1)
        line1 = random.randrange(0, self.size, 1)

        N1 = area * self.size + line1

        line2 = random.randrange(0, self.size, 1)

        while line1 == line2:
            line2 = random.randrange(0, self.size, 1)

        N2 = area * self.size + line1

        self.table[N1], self.table[N2] = self.table[N2], self.table[N1]

    def swap_colums_small(self):
        self.transporting()
        self.swap_rows_small()
        self.transporting()

    def swap_rows_area(self):
        area1 = random.randrange(0, self.size, 1)
        area2 = random.randrange(0, self.size, 1)

        while area1 == area2:
            area2 = random.randrange(0, self.size, 1)

        for i in range(0, self.size):
            N1, N2 = area1 * self.size + i, area2 * self.size + i
            self.table[N1], self.table[N2] = self.table[N2], self.table[N1]

    def swap_colums_area(self):
        self.transporting()
        self.swap_rows_area()
        self.transporting()

    def mix(self, amt=10):
        mix_func = [
            self.transporting,
            self.swap_rows_small,
            self.swap_colums_small,
            self.swap_rows_area,
            self.swap_colums_area
        ]
        for i in range(1, amt):
            id_func = random.randrange(0, 5, 1)
            mix_func[id_func]()

    def get(self):
        self.mix()
        return self.table


class Sudoku:
    def __init__(self):
        grid = Grid()
        self.grid = grid.get()
        self.user_grid = copy.deepcopy(self.grid)
        self.size = grid.size
        self.length = self.size * self.size

        self.mix_user_grid()

    def mix_user_grid(self):
        flook = [[0] * self.length for i in range(self.length)]
        iterator = 0
        difficult = self.length ** 2
        while iterator < difficult:
            i, j = random.randrange(0, self.length, 1), random.randrange(0, self.length, 1)
            if not flook[i][j]:
                iterator += 1
                flook[i][j] = 1

                temp = self.user_grid[i][j]
                self.user_grid[i][j] = 0

                difficult -= 1

                table_solution = []
                for copy_i in range(0, self.length):
                    table_solution.append(self.user_grid[copy_i][:])

                i_solution = 0
                for solution in solver.solve_sudoku((self.size, self.size), table_solution):
                    i_solution += 1

                if i_solution != 1:
                    self.user_grid[i][j] = temp
                    difficult += 1

    def check_game(self):
        for i in range(self.length):
            for j in range(self.length):
                if self.grid[i][j] != self.user_grid[i][j]:
                    return False
        return True

    def set_value(self, st, col, value):
        self.user_grid[st][col] = value

    def pprint(self):
        num = '   1 2 3 4 5 6 7 8 9'
        print(num)
        print(' ', '-' * 19)
        string = "{} |{} {} {}|{} {} {}|{} {} {}|"
        aab = 'ABCDEFGHI'

        count = 1
        for i in range(self.length):
            print(string.format(aab[i], *self.user_grid[i]))
            if not count % 3:
                print(' ', '-' * 19)
            count += 1

#if __name__ == '__main__':
#    print('Введите имя игрока: ')
#    player = input()
#    game_start = Wrapper(name = player)



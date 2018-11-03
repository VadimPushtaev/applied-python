import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint


class SnakeGame():

    def __init__(self):
        self.win_borders = (30, 60, 0, 0)
        self.snake = [(4,10), (4,9), (4,8)]
        self.key = KEY_RIGHT
        self.keys = (KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN)
        self.snake_ch = '*'
        score = 0


    def drop_apple(self, last_apple):
        while True:
            apple = randint(1, 18), randint(1, 58)
            if apple in self.snake:
                continue
            return apple

    @property
    def score(self):
        return len(self.snake) - 3

    def new_head(self):
        head = self.snake[0]

        # check key
        if self.key == KEY_RIGHT:
            new_head = head[0], head[1] + 1
        elif self.key == KEY_LEFT:
            new_head = head[0], head[1] - 1
        elif self.key == KEY_UP:
            new_head = head[0] - 1, head[1]
        elif self.key == KEY_DOWN:
            new_head = head[0] + 1, head[1]
        
        # check borders
        if new_head[0] == 0:
            new_head = self.win_borders[0] - 2, new_head[1]
        if new_head[0] == self.win_borders[0] - 1:
            new_head = 1, new_head[1]
        if new_head[1] == 0:
            new_head = new_head[0], self.win_borders[1] - 2
        if new_head[1] == self.win_borders[1] - 1:
            new_head = new_head[0], 1
        return new_head
    
    def loop(self, win):
        apple = self.drop_apple(None)
        win.addch(apple[0], apple[1], '#')
        while True:
            win.border(0)
            win.addstr(0, 2, 'Score : ' + str(self.score) + ' ')
            win.addstr(0, 27, ' SNAKE ')
            win.timeout(100)
    
            event = win.getch()
            if event == 27: # Escape
                break
            if event in self.keys:
                self.key = event

            head = self.new_head()
            win.addch(head[0], head[1], self.snake_ch)
            self.snake.insert(0, head)
            if apple in self.snake:
                apple = self.drop_apple(apple)
                win.addch(apple[0], apple[1], '#')
            else:
                tail = self.snake.pop()
                win.addch(tail[0], tail[1], ' ')

    def run(self):
        curses.initscr()
        win = curses.newwin(*self.win_borders)
        win.keypad(1)
        curses.noecho()
        curses.curs_set(0)
        win.border(0)
        win.nodelay(1)

        try:
            self.loop(win)
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(e)

        win.nodelay(0)
        win.keypad(0)
        curses.echo()
        curses.endwin()
        print("\nScore - " + str(self.score))


if __name__ == '__main__':
    SnakeGame().run()
import curses
from curses import KEY_RIGHT, KEY_LEFT


class ArkanoidGame:
    def __init__(self):
        self.win_borders = (30, 50, 0, 0)
        self.arc = [(25, 1), (25, 2), (25, 3), (25, 4), (25, 5)]
        self.ball = (self.arc_pos_y - 1, 3)
        self.delta = [-1, 1]
        self.name = 'ARKANOID'
        self.score = 0
        self.key = KEY_RIGHT
        self.arc_keys = (KEY_RIGHT, KEY_LEFT)
        self.ball_ch = 'o'
        self.snake_ch = '='

    @property
    def length(self):
        return len(self.arc)

    @property
    def arc_pos_y(self):
        return self.arc[0][0]

    def arc_pos(self):
        if self.key == KEY_RIGHT:
            new_x = self.arc[self.length - 1][1] + 1
            old_x = self.arc[0][1]
            if new_x < 49:
                self.arc.append((self.arc_pos_y, new_x))
                self.arc.pop(0)
            else:
                new_x = 49
        elif self.key == KEY_LEFT:
            new_x = self.arc[0][1] - 1
            old_x = self.arc[self.length - 1][1]
            if new_x > 0:
                self.arc.insert(0, (self.arc_pos_y, new_x))
                self.arc.pop()
            else:
                new_x = 0

        return (self.arc_pos_y, new_x), (self.arc_pos_y, old_x)

    def moving(self):
        old_y, old_x = self.ball[0], self.ball[1]
        new_y, new_x = old_y + self.delta[0], old_x + self.delta[1]

        if new_y in [0, 29]:
            self.delta[0] *= -1
            new_y, new_x = old_y + self.delta[0], old_x + self.delta[1]

        if new_x in [0, 49]:
            self.delta[1] *= -1
            new_y, new_x = old_y + self.delta[0], old_x + self.delta[1]

        self.ball = (new_y, new_x)
        return old_y, old_x

    def loop(self, win):
        for line in range(5, 12):
            for col in range(1, 49):
                win.addch(line, col, '@')
        for col in range(1, self.length + 1):
            win.addch(self.arc_pos_y, col, self.snake_ch)

        while True:
            win.border(0)
            win.addstr(0, 3, f' Score: {self.score} ')
            win.addstr(0, 23, f' {self.name} ')
            win.timeout(300)
            ball_old = self.moving()
            win.addch(self.ball[0], self.ball[1], self.ball_ch)
            # if (self.ball[0], self.ball[1]) != (ball_old[0], ball_old[1]):
            win.addch(ball_old[0], ball_old[1], ' ')
            event = win.getch()
            if event == 27:  # Escape
                break
            elif event in self.arc_keys:
                self.key = event
                new_pos, old_pos = self.arc_pos()
                if new_pos[1] not in [0, 49]:
                    win.addch(new_pos[0], new_pos[1], self.snake_ch)
                    win.addch(old_pos[0], old_pos[1], ' ')

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
        print(f"Score: {self.score}")


if __name__ == '__main__':
    ArkanoidGame().run()

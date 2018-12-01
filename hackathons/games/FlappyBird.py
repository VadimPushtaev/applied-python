import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint
import sys
sys.path.insert(0, "..")

import BaseGame

NAME = "FlappyBird"

class FlappyBird(BaseGame.BaseGame):
    @property
    def score(self):
        #if self.iteration > 44:
        return self.iteration // 4

    def new_bird(self):
        new_bird = self.bird
        # check key
        if self.key == KEY_UP:
            new_bird = self.bird[0]-5, self.bird[1]
        elif self.key == -1:
            new_bird = self.bird[0]+1, self.bird[1]
        return new_bird

    def drop_barrier(self):
        return self.win_borders[0]//2 + randint(0, self.dist) - self.dist

    def print_barr(self, win, y1, y2, x1, width):
        for i in range(1,self.win_borders[0]-1):
                if i not in range(y1,y2):
                    win.addstr(i, x1, '='*10)
                    win.addstr(i, x1+width, ' '*10)

    def clear_left_border(self, win):
        for i in range(1, self.win_borders[0]-1):
            win.addch(i,1, ' ')
    
    def loop(self, win):
        barr = self.drop_barrier()
        self.barriers.append([barr, barr+self.dist])
        z = 3
        while True:
            self.iteration += 1
            win.border(0)
            win.addstr(0, 2, 'Score : ' + str(self.score) + ' ')
            win.addstr(0, 20, ' FLAPPY BIRD ')
            win.timeout(200)
    
            event = win.getch()
            if event == 27: # Escape
                break
            if event in self.keys:
                self.key = event

            bird = self.new_bird()
            win.addch(bird[0], bird[1], self.bird_ch)
            win.addch(self.bird[0], self.bird[1], ' ')
            self.bird = bird
            #self.add_scores(self.score)
            count = len(self.barriers)
            for idx, b in enumerate(self.barriers):
                if self.win_borders[1]-8*(count-idx)-1 < 1:
                    self.barriers.pop(0)
                    continue
                self.print_barr(win, b[0], b[1], self.win_borders[1]-8*(count-idx)-1, 4)
            self.clear_left_border(win)
            if self.iteration % 8:
                continue
            barr = self.drop_barrier()
            self.barriers.append([barr, barr+self.dist])
            

    def run(self):
        self.win_borders = (30, 60, 0, 0) #no constructor = more pain
        self.bird = [9,10]
        self.barriers = []
        self.key = -1
        self.keys = [KEY_UP, -1]
        self.bird_ch = '*'
        self.dist = 7
        self.jump = 5
        self.iteration = -1
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
        self.add_scores(self.score)
        print("\nScore - " + str(self.score))


if __name__ == '__main__':
    FlappyBird(NAME, FlappyBird.score).run()
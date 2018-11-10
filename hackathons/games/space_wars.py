import os
import random

import arcade

from BaseGame import BaseGame

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

SPRITE_SCALING_PLAYER = 0.2
SPRITE_SCALING_ENEMY = 0.1
SPRITE_SCALING_SHOT = 0.08

MOVEMENT_SPEED = 3
ENEMY_MOVEMENT_SPEED = 120
ENEMY_SCREEN_SPACING = 40

SHOT_MOVEMENT_SPEED = 200

ENEMY_GENERATION_PROBABILITY = 0.02

GAME_TIME = 20

NAME = "Space wars 3000"

IMG_FOLDER = os.path.join("games", "space_wars_img")  # path changed so that tester.py will se images folder


class Game(BaseGame):

    def run(self):
        game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
        game.setup()
        arcade.run()
        self.add_scores(game.score)


class Player(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1


class Enemy(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1


class Shot(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)
        self.background = None

        self.enemy_list = arcade.SpriteList()
        self.shot_list = arcade.SpriteList()

        self.player_sprite = Player(os.path.join(IMG_FOLDER, "player.png"), SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 150
        self.player_sprite.center_y = SCREEN_HEIGHT/2

        self.score = 0
        self.total_time = 0.0
        self.running = True
        self.win = False

    def setup(self):
        self.background = arcade.load_texture(os.path.join(IMG_FOLDER, "background.jpg"))

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        if self.running:

            self.player_sprite.draw()

            for enemy in self.enemy_list:
                enemy.draw()
            for shot in self.shot_list:
                shot.draw()
            arcade.draw_text("Score: " + str(self.score), 10, 30, arcade.color.WHITE, 12)
            arcade.draw_text("Time left: " + str(round(GAME_TIME - self.total_time,1)), 10, 10, arcade.color.WHITE, 12)
        else:
            if self.win:
                arcade.draw_text("YOU WON! Score: " + str(self.score), SCREEN_WIDTH / 2 - 200, SCREEN_HEIGHT / 2, arcade.color.WHITE, 30)
            else:
                arcade.draw_text("Game OVER", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 100, arcade.color.WHITE, 30)

    def update(self, delta_time):
        if self.running:
            self.player_sprite.update()
            for enemy in self.enemy_list:
                enemy.change_x = - ENEMY_MOVEMENT_SPEED * delta_time
                enemy.change_y = 0

                enemy.update()

            for shot in self.shot_list:
                shot.change_x = SHOT_MOVEMENT_SPEED * delta_time
                shot.change_y = 0
                shot.update()

            if random.random() < ENEMY_GENERATION_PROBABILITY:
                enemy_sprite = Enemy(os.path.join(IMG_FOLDER, "enemy.png"), SPRITE_SCALING_ENEMY)
                self.enemy_list.append(enemy_sprite)
                enemy_sprite.center_x = SCREEN_WIDTH
                enemy_sprite.center_y = random.randint(ENEMY_SCREEN_SPACING, SCREEN_HEIGHT-ENEMY_SCREEN_SPACING)

            for enemy in self.enemy_list:
                for shot in self.shot_list:
                    if arcade.check_for_collision(enemy, shot):
                        self.enemy_list.remove(enemy)
                        self.shot_list.remove(shot)
                        self.score += 1
                if enemy.center_x - enemy.width/2 < 0:
                    self.stop_game()

            self.total_time += delta_time
            if self.total_time > GAME_TIME:
                self.win = True
                self.stop_game()

    def stop_game(self):
        self.running = False

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED
        elif key == arcade.key.SPACE:
            shot_sprite = Shot(os.path.join(IMG_FOLDER, "shot.png"), SPRITE_SCALING_SHOT)
            shot_sprite.center_x = self.player_sprite.center_x + self.player_sprite.width/2
            shot_sprite.center_y = self.player_sprite.center_y
            self.shot_list.append(shot_sprite)

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()

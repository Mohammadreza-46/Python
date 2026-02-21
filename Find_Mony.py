import time
from pygame import mixer
import pygame
import os

screen = pygame.display.set_mode((1, 1))
dir = os.path.dirname(__file__)
class Game:
    def __init__(self):
        self.map = [
            ['🧱', '🧱', '$', '.', '.', '.', '$'],
            ['.', '.', '.', '.', '.', '🧱', '.'],
            ['.', '.', '.', '🧱', '.', '$', '.'],
            ['🧱', '$', '.', '.', '.', '.', '.'],
            ['🧱', '🧱', '🧱', '.', '.', '🧱', '$'],
            ['🧱', '🧱', '.', '.', '.', '🧱', '🧱'],
            ['🧱', '🧱', '$', '.', '.', '🧱', '🧱'],
            ['🧱', '🧱', '🧱', '.', '$', '🧱', '🧱']
        ]
        self.player = Player(4,4)
        self.treasures = 7
        self.map[self.player.y][self.player.x] = 'p'
    def print_map(self):
        print('\n'+'='*30)
        for i in self.map:
            print(''.join(i))
        print('='*30)
        print(f'score: {self.player.score}')
        print('='*30+'\n')
    # this file has sound if file your system has file sound open it
    # sound file is in the GitHub
    def game_over(self):
        print('Game Over!')
        try:
            mixer.init()
            music = mixer.Sound(os.path.join(dir,'Game_Over.mp3'))
            music.play()
            time.sleep(3)
            exit()
        except FileNotFoundError:
            exit()
        except:
            exit()
    def win(self):
        print('You win!')
        try:
            mixer.init()
            music = mixer.Sound(os.path.join(dir,'Win.mp3'))
            music.play()
            time.sleep(3)
        except FileNotFoundError:
            return
        except:
            return
    def coin(self):
        if self.player.score >= 6:
            self.treasures -= 1
            self.player.score += 1
            return
        try:
            self.treasures -= 1
            self.player.score += 1
            mixer.init()
            music = mixer.Sound(os.path.join(dir,'Coin.mp3'))
            music.play()
        except FileNotFoundError:
            self.treasures -= 1
            self.player.score += 1
        except:
            self.treasures -= 1
            self.player.score += 1
    def error_move(self, x , y):
        if y < 0 or y >=len(self.map):
            return False
        if x < 0 or x >=len(self.map[y]):
            return False
        if self.map[y][x] == '🧱':
            print('you touch the 🧱')
            return False
        else:
            return True
    def move_player(self, direction):
        old_x = self.player.x
        old_y = self.player.y
        new_x = self.player.x
        new_y = self.player.y
        if direction == 'w':
            new_y -= 1
        elif direction == 's':
            new_y += 1
        elif direction == 'd':
            new_x += 1
        elif direction == 'a':
            new_x -= 1
        else:
            print('Key is not w,s,a,d')
        if not self.error_move(new_x,new_y):
            self.game_over()
            return
        self.player.x = new_x
        self.player.y = new_y
        if self.map[new_y][new_x] == '$':
            self.coin()


        self.player.x = new_x
        self.player.y = new_y
        self.map[old_y][old_x] = '.'
        self.map[new_y][new_x] = 'p'

    def play(self):
        print('Welcome to Game\n')
        pygame.init()
        self.print_map()
        while self.treasures > 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.move_player('w')
                        self.print_map()
                    elif event.key == pygame.K_s:
                        self.move_player('s')
                        self.print_map()
                    elif event.key == pygame.K_d:
                        self.move_player('d')
                        self.print_map()
                    elif event.key == pygame.K_a:
                        self.move_player('a')
                        self.print_map()
                    elif event.key == pygame.K_e:
                        __ = input('Do you want to exit? (y/n):').lower()
                        if __ == 'y':
                         self.game_over()
                        elif __ == 'n':
                            self.print_map()
                            continue
        self.print_map()
        self.win()
class Player:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.score = 0


if __name__ == '__main__':
    game = Game()
    game.play()
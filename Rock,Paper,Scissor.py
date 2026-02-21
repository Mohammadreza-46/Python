class Player:
    def __init__(self, name):
        self.name = name
        self.choose = None
    def player_choose(self):
        print('\nfor rock write 1 for paper write 2 for scissor write 3')
        choice = int(input(f'{self.name} what is your choice?: '))
        if choice == 1:
            self.choose = 'rock'
        elif choice == 2:
            self.choose = 'paper'
        elif choice == 3:
            self.choose = 'scissor'
        else:
            raise ValueError('invalid choice')
class Computer():
    def __init__(self):
        self.choose = None
    def computer_choose(self):
        import random
        number = random.randint(1,3)
        if number == 1:
            self.choose = 'rock'
        elif number == 2:
            self.choose = 'paper'
        elif number == 3:
            self.choose = 'scissor'
class Game:
    def __init__(self, player_name):
        self.player = Player(player_name)
        self.computer = Computer()
        self.player_score = 0
        self.computer_score = 0
        self.round = 1
    def winner(self):
        self.player.player_choose()
        self.computer.computer_choose()
        if self.computer.choose == self.player.choose:
            print(f'round:{self.round} ==')
            return
        elif (self.computer.choose == 'rock' and self.player.choose == 'scissor')or (self.computer.choose == 'paper' and self.player.choose == 'rock') or (self.computer.choose == 'scissor' and self.player.choose == 'paper'):
            print(f'round:{self.round}, winner:computer')
            self.computer_score += 1
        else:
            print(f'round:{self.round}, winner:{self.player.name}')
            self.player_score += 1
    def round_(self):
        self.winner()
        print(f'{self.player.name} choose: {self.player.choose}\n',
              f' computer choose: {self.computer.choose}')
        print(f'\n{self.player.name} score: {self.player_score}',
              f'\ncomputer score: {self.computer_score}')
        self.round += 1
    def play(self):
        while self.player_score != 3 and self.computer_score != 3:
            self.round_()
        if self.player_score > self.computer_score:
            print(f'{self.player.name} is the winner!')
        elif self.player_score < self.computer_score:
            print('computer is the winner!','\n You lose!')
if __name__ == '__main__':
    game = Game(input('Enter your name: '))
    game.play()

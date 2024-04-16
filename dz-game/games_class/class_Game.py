from .class_Hero import Hero
class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print("Игра начинается!")
        while self.player.is_alive() and self.computer.is_alive():
            self.player.attack(self.computer)
            if not self.computer.is_alive():
                print(f"{self.player.name} победил!")
                break
            self.computer.attack(self.player)
            if not self.player.is_alive():
                print("Компьютер победил!")
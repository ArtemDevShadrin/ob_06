from games_class.class_Game import Game

if __name__ == "__main__":
    player_name = input("Введите имя игрока: ")
    game = Game(player_name)
    game.start()
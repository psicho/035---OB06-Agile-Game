import random

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} на {self.attack_power} урона!")

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер", attack_power=random.randint(15, 25))

    def start(self):
        print(f"\nДобро пожаловать в 'Битву героев', {self.player.name}!")
        print("Правила: Герой и Компьютер по очереди атакуют друг друга.\n")

        turn = 0
        while self.player.is_alive() and self.computer.is_alive():
            print(f"\n--- Раунд {turn + 1} ---")
            if turn % 2 == 0:
                self.player.attack(self.computer)
                print(f"У {self.computer.name} осталось здоровья: {max(0, self.computer.health)}")
            else:
                self.computer.attack(self.player)
                print(f"У {self.player.name} осталось здоровья: {max(0, self.player.health)}")
            turn += 1

        print("\n=== Игра окончена! ===")
        if self.player.is_alive():
            print(f"Победил {self.player.name}!")
        else:
            print("Победил Компьютер!")

if __name__ == "__main__":
    player_name = input("Введите имя героя: ")
    game = Game(player_name)
    game.start()

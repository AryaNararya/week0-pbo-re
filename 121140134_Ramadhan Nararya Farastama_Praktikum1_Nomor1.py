import random

class Robot:
    def __init__(self, name, hp, attack, accuracy):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.accuracy = accuracy  # Persentase akurasi serangan (0-100)

    def attack_enemy(self, enemy):
        if random.randint(0, 100) <= self.accuracy:  # Cek apakah serangan mengenai
            damage = random.randint(self.attack // 2, self.attack)  # Damage acak dalam rentang
            enemy.hp -= damage
            print(f"{self.name} menyerang {enemy.name} dan memberikan {damage} damage!")
            print(f"{enemy.name} memiliki {enemy.hp} HP tersisa.\n")
        else:
            print(f"{self.name} menyerang {enemy.name}, tetapi serangannya meleset!\n")

    def regen_health(self):
        heal_amount = random.randint(5, 15)  # Jumlah HP yang diregenerasi
        self.hp += heal_amount
        print(f"{self.name} melakukan regenerasi dan memulihkan {heal_amount} HP!")
        print(f"{self.name} sekarang memiliki {self.hp} HP.\n")

    def is_alive(self):
        return self.hp > 0


class Game:
    def __init__(self, robot1, robot2, max_rounds=10):
        self.robot1 = robot1
        self.robot2 = robot2
        self.max_rounds = max_rounds

    def start(self):
        print("Pertarungan Robot dimulai!\n")
        for round in range(1, self.max_rounds + 1):
            print(f"=== Ronde {round} ===")
            # Robot 1 menyerang Robot 2
            self.robot1.attack_enemy(self.robot2)
            if not self.robot2.is_alive():
                print(f"{self.robot2.name} telah dikalahkan! {self.robot1.name} menang!\n")
                break

            # Robot 2 menyerang Robot 1
            self.robot2.attack_enemy(self.robot1)
            if not self.robot1.is_alive():
                print(f"{self.robot1.name} telah dikalahkan! {self.robot2.name} menang!\n")
                break

            # Kesempatan untuk regenerasi HP
            if random.randint(0, 100) <= 30:  # 30% chance untuk regenerasi
                self.robot1.regen_health()
            if random.randint(0, 100) <= 30:
                self.robot2.regen_health()

            print("=" * 20 + "\n")

        if self.robot1.is_alive() and self.robot2.is_alive():
            print("Pertarungan berakhir seri!\n")


# Membuat robot
robot1 = Robot(name="Lucifer 'Rezael'", hp=100, attack=20, accuracy=80)
robot2 = Robot(name="Minato Sakai", hp=100, attack=18, accuracy=75)

# Memulai permainan
game = Game(robot1, robot2)
game.start()
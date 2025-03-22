from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, age):
        if not name.strip():
            raise ValueError("Nama hewan tidak boleh kosong.")
        if age <= 0:
            raise ValueError("Usia hewan harus lebih dari 0.")
        self.__name = name
        self.__age = age

    @abstractmethod
    def make_sound(self):
        pass

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if not name.strip():
            raise ValueError("Nama hewan tidak boleh kosong.")
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age <= 0:
            raise ValueError("Usia hewan harus lebih dari 0.")
        self.__age = age

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

    def fetch(self):
        return f"{self.get_name()} is fetching the ball."

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

    def climb(self):
        return f"{self.get_name()} is climbing the tree."

class Bird(Animal):
    def make_sound(self):
        return "Chirp!"

    def fly(self):
        return f"{self.get_name()} is flying."

class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.get_name()} telah ditambahkan ke kebun binatang.")

    def show_animals(self):
        if not self.animals:
            print("Tidak ada hewan di kebun binatang.")
        else:
            print("Hewan di Kebun Binatang:")
            for animal in self.animals:
                print(f"{animal.get_name()} ({animal.__class__.__name__}): {animal.make_sound()}")

def main():
    zoo = Zoo()
    while True:
        print("\nPilih aksi:")
        print("1. Tambah hewan")
        print("2. Tampilkan hewan")
        print("3. Keluar")
        try:
            choice = input("Masukkan pilihan (1/2/3): ")
            if choice == '1':
                print("Pilih jenis hewan:")
                print("1. Anjing")
                print("2. Kucing")
                print("3. Burung")
                animal_type = input("Masukkan pilihan (1/2/3): ")
                name = input("Masukkan nama hewan: ")
                age = int(input("Masukkan usia hewan: "))
                if animal_type == '1':
                    animal = Dog(name, age)
                elif animal_type == '2':
                    animal = Cat(name, age)
                elif animal_type == '3':
                    animal = Bird(name, age)
                else:
                    print("Pilihan tidak valid.")
                    continue
                zoo.add_animal(animal)
            elif choice == '2':
                zoo.show_animals()
            elif choice == '3':
                print("Keluar dari program.")
                break
            else:
                print("Pilihan tidak valid. Harap masukkan angka antara 1 dan 3.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    main()
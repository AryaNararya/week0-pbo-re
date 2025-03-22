import math

def get_positive_number():
    while True:
        try:
            number = float(input("Masukkan angka: "))
            if number < 0:
                print("Input tidak valid. Harap masukkan angka positif.")
            elif number == 0:
                print("Error: Akar kuadrat dari nol tidak diperbolehkan.")
            else:
                return number
        except ValueError:
            print("Input tidak valid. Harap masukkan angka yang valid.")

def main():
    number = get_positive_number()
    sqrt = math.sqrt(number)
    print(f"Akar kuadrat dari {number} adalah {sqrt}.")

if __name__ == "__main__":
    main()
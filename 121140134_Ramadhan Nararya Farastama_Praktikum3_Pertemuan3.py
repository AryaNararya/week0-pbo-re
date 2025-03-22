class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if not task.strip():
            raise ValueError("Tugas tidak boleh kosong.")
        self.tasks.append(task)
        print("Tugas berhasil ditambahkan!")

    def remove_task(self, task_number):
        if task_number < 1 or task_number > len(self.tasks):
            raise IndexError(f"Error: Tugas dengan nomor {task_number} tidak ditemukan.")
        self.tasks.pop(task_number - 1)
        print("Tugas berhasil dihapus!")

    def show_tasks(self):
        if not self.tasks:
            print("Daftar tugas kosong.")
        else:
            print("Daftar Tugas:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

def main():
    manager = TaskManager()
    while True:
        print("\nPilih aksi:")
        print("1. Tambah tugas")
        print("2. Hapus tugas")
        print("3. Tampilkan daftar tugas")
        print("4. Keluar")
        try:
            choice = input("Masukkan pilihan (1/2/3/4): ")
            if choice == '1':
                task = input("Masukkan tugas yang ingin ditambahkan: ")
                manager.add_task(task)
            elif choice == '2':
                manager.show_tasks()
                if manager.tasks:
                    task_number = int(input("Masukkan nomor tugas yang ingin dihapus: "))
                    manager.remove_task(task_number)
            elif choice == '3':
                manager.show_tasks()
            elif choice == '4':
                print("Keluar dari program.")
                break
            else:
                print("Pilihan tidak valid. Harap masukkan angka antara 1 dan 4.")
        except ValueError as e:
            print(e)
        except IndexError as e:
            print(e)
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    main()
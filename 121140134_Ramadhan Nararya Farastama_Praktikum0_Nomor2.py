# Inisialisasi dictionary untuk menyimpan data siswa
data_siswa = {}

# Jumlah siswa yang akan diinput
jumlah_siswa = int(input("Masukkan jumlah siswa: "))

# Loop untuk mengisi data siswa
for i in range(jumlah_siswa):
    nama = input(f"Masukkan nama siswa ke-{i+1}: ")
    nilai = float(input(f"Masukkan nilai {nama}: "))
    
    # Menambahkan data siswa ke dalam dictionary
    data_siswa[nama] = nilai

# Menampilkan data siswa yang telah diinput
print("\nData Siswa:")
for nama, nilai in data_siswa.items():
    print(f"{nama}: {nilai}")
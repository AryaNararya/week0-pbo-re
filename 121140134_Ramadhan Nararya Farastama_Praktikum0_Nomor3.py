# Meminta input dari pengguna
nama = input("Masukkan nama Anda: ")
umur = input("Masukkan umur Anda: ")
hobi = input("Masukkan hobi Anda: ")
cita_cita = input("Masukkan cita-cita Anda: ")

# Membuka file dengan mode 'w' (write) untuk menulis data
with open("data_diri.txt", "w") as file:
    # Menulis data ke dalam file
    file.write(f"Nama: {nama}\n")
    file.write(f"Umur: {umur} tahun\n")
    file.write(f"Hobi: {hobi}\n")
    file.write(f"Cita-cita: {cita_cita}\n")

print("File 'data_diri.txt' telah berhasil dibuat dan data telah ditulis.")
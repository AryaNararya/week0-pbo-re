# Input tinggi segitiga
height = 5

# Loop untuk membuat segitiga
for i in range(1, height + 1):
    # Mencetak spasi untuk membuat bentuk segitiga
    for j in range(height - i):
        print(" ", end="")
    
    # Mencetak bintang untuk membentuk segitiga
    for k in range(2 * i - 1):
        print("*", end="")
    
    # Pindah ke baris berikutnya
    print()
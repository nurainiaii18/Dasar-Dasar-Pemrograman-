# tugas no1
kendaraan = ["honda", "Motor", "3000cc", "hitam", "2roda"]
print("list awal: ")
tambahan = [3000, "matic"]
kendaraan.extend(tambahan)
kendaraan.insert(2, "honda")
print(kendaraan)

# tugas no 2
print("=== Alat hitung luas bangun datar ===")
print("pilih 1 untuk menghitung luas persegi")
print("pilih 2 untuk menghitung luas lingkaran")
print("pilih 3 untuk menghitung luas segitiga")

pilihan = int(input("Masukkan pilihan (1/2/3)"))
match pilihan:
    case 1:
        s = int(input("Masukkan panjang sisi persegi"))
        luas = s * s
        print(f"Luas persegi adalah: {luas}")
   
    case 2:
        r = int(input("Masukkan panjang jari-jari lingkaran: "))
        pi = 3.14
        luas = pi * r**2
        print(f"Luas lingkaran adalah: {luas}")
    
    case 3:
        a = int(input("Masukkan panjang alas segitiga:"))
        t = int(input("Masukkan panjang tinggi segitiga:"))
        luas = a * t / 2
        print(f"Luas segitiga adalah: {luas}")
        1
    case _:
        print("Masukkan pilihan dengan benar")

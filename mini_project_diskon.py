# MINI PROJECT Praktikum Dasar Pemrograman
# Nama  : Aris Candra Muzaffar
# NIM   : 2409116088


# Nilai tambahan jika menerapkan login sederhana (input nama, nim, dan lainnya)
print("____________________________________")
print("PROGRAM KALKULASI TOTAL HARGA BARANG")
print("_____Oleh Aris Candra Muzaffar______")
print("________Sistem Informasi '24________")
print("____________________________________")

# Menggunakan perulangan agar user bisa mencoba login lagi jika gagal
while True:
    print("_______________LOGIN________________")
    nama = str(input("Masukkan Nama Anda: "))
    nim = str(input("Masukkan 3 Digit Akhir NIM Anda: "))
    if nama == "Aris" and nim == "088":
        print("Selamat datang, ",nama,"Candra Muzaffar"," Dengan NIM 2409116"+nim)
        break  # keluar jika berhasil
    else:
        print("Nama atau NIM anda tidak dikenal")
        pilihan = input("Apakah Anda ingin mencoba login lagi? (y/n): ")
        if pilihan != 'y':
            print("Program selesai.")
            exit()  # keluar dari program jika tidak ingin login lagi

# Menggunakan input untuk harga barang dan jumlah pembelian
while True:
    print("Masukkan 0 pada harga barang, jika anda ingin keluar dari program")
    hargaBarang = int(input("Masukkan harga barang: Rp. "))
    # Menerapkan perulangan untuk memberikan pilihan apakah ingin menghitung total harga lagi atau keluar dari program
    # Periksa jika pengguna ingin keluar
    if hargaBarang == 0:
        print("Program selesai.")
        break  # keluar dari program

    jumlahBarang = int(input("Masukkan jumlah barang yang dibeli: "))
    
    total = hargaBarang * jumlahBarang
    kondisi = 250000

# Membuat percabangan untuk menentukan apakah total harga barang lebih dari Rp. 250.000. Jika lebih, tambahkan diskon sebesar 25%. Sedangkan jika tidak mencapai lebih dari Rp.250.000, maka tidak mendapatkan diskon
    if total > kondisi:
        harga_akhir = total - (0.25 * total)
        print("Selamat, Anda Mendapatkan Diskon 25%")
        print("Total harga adalah: Rp. ",harga_akhir)
    else:
        print("Total harga adalah: Rp. ",total)

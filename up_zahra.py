print("===================================")
print("   SISTEM PENGELOLAAN STOK BARANG")
print("===================================")

# 1. Input data barang
nama_barang = input("Masukkan nama barang: ")
stok = int(input("Masukkan jumlah stok awal: "))

# 2. Proses transaksi berulang
while True:
    print("\n===== PILIH TRANSAKSI =====")
    print("1. Barang Masuk")
    print("2. Barang Keluar")
    print("3. Selesai")

    pilihan = input("Pilih transaksi (1/2/3): ")

    # 3. Menentukan transaksi
    if pilihan == "1":
        jumlah = int(input("Masukkan jumlah barang masuk: "))
        stok = stok + jumlah
        print("Barang berhasil ditambahkan!")
        print("Stok sekarang:", stok)

    elif pilihan == "2":
        jumlah = int(input("Masukkan jumlah barang keluar: "))

        # 4. Mengecek ketersediaan stok
        if jumlah <= 0:
            print("Jumlah barang harus lebih dari 0!")
        elif jumlah <= stok:
            stok = stok - jumlah
            print("Barang berhasil dikeluarkan!")
            print("Stok sekarang:", stok)
        else:
            print("Stok Tidak Mencukupi!")

    elif pilihan == "3":
        print("\nTransaksi selesai!")
        break

    else:
        print("Pilihan tidak tersedia!")

# 5. Menampilkan hasil akhir
print("\n===================================")
print("         HASIL AKHIR STOK")
print("===================================")
print("Nama Barang :", nama_barang)
print("Stok Akhir  :", stok)
print("===================================")
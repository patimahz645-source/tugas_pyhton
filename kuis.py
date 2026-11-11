# program kelulusan ujian mahasiwa

nama = input("Masukkan nama Mahasiswa: ")

# Menentukan target nilai

if nama.lower() == "andi" :
    target = 70 
elif nama.lower() =="budi" :
    target = 75
elif nama.lower() == "citra" :
    target = 80
else: 

    target = None
    print ("Nama mahasiswa tidak terdaftar!")

# jika nama terdaftar
if target is not None: 
    print("nama mahasiswa:" , nama)
    print("target nilai:" , target)

    percobaan = 1

    while percobaan <= 3:
        nilai = int(input(f"masukkan nilai percobaan ke-{percobaan} : "))

        if nilai >= target:
            print(f"{nama} berhasil lulus!")
            print(f"lulus pada percobaan ke-{percobaan}.")
            break
        else:
            print("masukkan nilai target.")
        percobaan += 1
    if percobaan > 3:
        print(f"{nama} dinyatakan tidak lulus!")
        print("sudah mencapai batas 3 kali percobaan.")
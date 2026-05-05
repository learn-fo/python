"""
- Input dan Output
- Deklarasi & Inisialisasi Variabel
- Variabel Lokal & Global
- Tipe Data
- Mengubah Variabel
"""

# ============================================================
# 1. DEKLARASI DAN INISIALISASI VARIABEL
# ============================================================
print("\n1. DEKLARASI & INISIALISASI VARIABEL")
print("-" * 40)

# Deklarasi + inisialisasi (Python tidak perlu deklarasi terpisah)
nama = "Budi"           # string
umur = 20               # integer
tinggi = 165.5          # float
is_mahasiswa = True     # boolean

print(f"Nama: {nama}")
print(f"Umur: {umur}")
print(f"Tinggi: {tinggi} cm")
print(f"Mahasiswa: {is_mahasiswa}")

# Multiple assignment (inisialisasi banyak variabel sekaligus)
a, b, c = 1, 2, 3
print(f"\nMultiple assignment: a={a}, b={b}, c={c}")

# Assign nilai yang sama
x = y = z = 100
print(f"Nilai sama: x={x}, y={y}, z={z}")


# ============================================================
# 2. TIPE DATA DASAR
# ============================================================
print("\n2. TIPE DATA DASAR")
print("-" * 40)

# Integer (bilangan bulat)
angka_bulat = 100
print(f"Integer: {angka_bulat} -> tipe: {type(angka_bulat)}")

# Float (bilangan desimal)
angka_desimal = 3.14
print(f"Float: {angka_desimal} -> tipe: {type(angka_desimal)}")

# String (teks)
teks = "Hello Python"
print(f"String: {teks} -> tipe: {type(teks)}")

# Boolean (True/False)
status = True
print(f"Boolean: {status} -> tipe: {type(status)}")

# List (kumpulan data)
list_data = [1, 2, 3, 4]
print(f"List: {list_data} -> tipe: {type(list_data)}")

# Tuple (sama seperti list tapi tidak bisa diubah)
tuple_data = (1, 2, 3)
print(f"Tuple: {tuple_data} -> tipe: {type(tuple_data)}")

# Dictionary (key-value pair)
dict_data = {"nama": "Budi", "umur": 20}
print(f"Dictionary: {dict_data} -> tipe: {type(dict_data)}")


# ============================================================
# 3. INPUT DARI USER
# ============================================================
print("\n3. INPUT DARI USER")
print("-" * 40)

# Input selalu menghasilkan string
nama_user = input("Masukkan nama Anda: ")
umur_user = input("Masukkan umur Anda: ")

print(f"\nHalo {nama_user}!")
print(f"Umur Anda {umur_user} tahun")

# Konversi input ke tipe data lain
angka1 = int(input("\nMasukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))
hasil = angka1 + angka2
print(f"Hasil penjumlahan: {angka1} + {angka2} = {hasil}")


# ============================================================
# 4. OUTPUT / PRINT
# ============================================================
print("\n4. OUTPUT / PRINT")
print("-" * 40)

# Cara 1: print biasa
print("Cara 1: Hello World")

# Cara 2: print dengan variabel
nama = "Siti"
print("Cara 2: Halo", nama)

# Cara 3: f-string (paling direkomendasikan)
usia = 25
print(f"Cara 3: Halo {nama}, usia {usia} tahun")

# Cara 4: format()
print("Cara 4: Halo {}, usia {} tahun".format(nama, usia))

# Cara 5: concatenation (+)
print("Cara 5: Halo " + nama + ", usia " + str(usia) + " tahun")

# Print tanpa newline
print("Ini ", end="")
print("satu baris")

# Print dengan separator
print("a", "b", "c", sep=" - ")


# ============================================================
# 5. MENGUBAH VARIABEL (TYPE CASTING)
# ============================================================
print("\n5. MENGUBAH TIPE DATA (TYPE CASTING)")
print("-" * 40)

nilai_string = "100"
print(f"Nilai awal (string): '{nilai_string}' -> tipe: {type(nilai_string)}")

# String ke Integer
nilai_int = int(nilai_string)
print(f"String ke Int: {nilai_int} -> tipe: {type(nilai_int)}")

# String ke Float
nilai_float = float(nilai_string)
print(f"String ke Float: {nilai_float} -> tipe: {type(nilai_float)}")

# Integer ke String
angka = 50
angka_string = str(angka)
print(f"Int ke String: '{angka_string}' -> tipe: {type(angka_string)}")

# Integer ke Float
int_ke_float = float(angka)
print(f"Int ke Float: {int_ke_float} -> tipe: {type(int_ke_float)}")

# Float ke Integer (membulatkan ke bawah)
desimal = 3.14
float_ke_int = int(desimal)
print(f"Float ke Int: {float_ke_int} -> tipe: {type(float_ke_int)}")


# ============================================================
# 6. VARIABEL LOKAL DAN GLOBAL
# ============================================================
print("\n6. VARIABEL LOKAL DAN GLOBAL")
print("-" * 40)

# Variabel global (bisa diakses di mana saja)
versi = "Python 3"
nama_program = "Belajar Variabel"

def tampilkan_global():
    # Mengakses variabel global (cukup baca)
    print(f"Versi: {versi}")
    print(f"Program: {nama_program}")

def ubah_global():
    global versi  # wajib pakai global jika ingin mengubah
    versi = "Python 3.12"
    print(f"Versi diubah menjadi: {versi}")

def fungsi_lokal():
    # Variabel lokal (hanya ada di fungsi ini)
    lokal = "Ini variabel lokal"
    print(f"Di dalam fungsi: {lokal}")
    # print(lokal)  # Bisa diakses di dalam fungsi
    return lokal

print("=== Sebelum mengubah global ===")
tampilkan_global()

print("\n=== Mengubah variabel global ===")
ubah_global()

print("\n=== Setelah mengubah global ===")
tampilkan_global()

print("\n=== Variabel lokal ===")
hasil_lokal = fungsi_lokal()
# print(lokal)  # ERROR! Tidak bisa diakses di luar fungsi


# ============================================================
# 7. MENGUBAH NILAI VARIABEL
# ============================================================
print("\n7. MENGUBAH NILAI VARIABEL")
print("-" * 40)

# Langsung assign nilai baru
angka = 10
print(f"Nilai awal: {angka}")

angka = 20
print(f"Nilai baru: {angka}")

# Ubah tipe data juga bisa
data = 100
print(f"data = {data}, tipe: {type(data)}")

data = "Sekarang jadi string"
print(f"data = {data}, tipe: {type(data)}")

data = 3.14
print(f"data = {data}, tipe: {type(data)}")

# Menggunakan augmented assignment
nilai = 5
print(f"\nNilai awal: {nilai}")
nilai += 2  # nilai = nilai + 2
print(f"nilai += 2 -> {nilai}")
nilai -= 1  # nilai = nilai - 1
print(f"nilai -= 1 -> {nilai}")
nilai *= 3  # nilai = nilai * 3
print(f"nilai *= 3 -> {nilai}")

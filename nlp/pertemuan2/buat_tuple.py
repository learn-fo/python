# TUPLE

# ============================================================
# 1. MEMBUAT TUPLE (DEKLARASI & INISIALISASI)
# ============================================================
print("\n1. MEMBUAT TUPLE")
print("-" * 40)

# Tuple kosong
tuple_kosong = ()
print(f"Tuple kosong: {tuple_kosong}")

# Tuple dengan kurung
angka = (1, 2, 3, 4, 5)
print(f"Tuple angka: {angka}")

# Tuple tanpa kurung (tuple packing)
buah = "apel", "mangga", "jeruk"
print(f"Tuple buah: {buah}")

# Tuple dengan 1 elemen (WAJIB pakai koma)
satu_elemen = (10,)
print(f"Tuple 1 elemen: {satu_elemen}")

# Bukan tuple (ini integer)
bukan_tuple = (10)
print(f"Tanpa koma jadi integer: {bukan_tuple} -> tipe: {type(bukan_tuple)}")

# Tuple dengan tipe data berbeda
campuran = (10, "Budi", 3.14, True)
print(f"Tuple campuran: {campuran}")

# Tuple dari list
list_angka = [1, 2, 3]
tuple_dari_list = tuple(list_angka)
print(f"Tuple dari list {list_angka}: {tuple_dari_list}")

# Tuple dari string
tuple_dari_string = tuple("Python")
print(f"Tuple dari string 'Python': {tuple_dari_string}")


# ============================================================
# 2. MENGAKSES ELEMEN TUPLE
# ============================================================
print("\n2. MENGAKSES ELEMEN TUPLE")
print("-" * 40)

buah = ("apel", "mangga", "jeruk", "anggur", "pisang")
print(f"Tuple buah: {buah}\n")

# Akses berdasarkan index (mulai dari 0)
print(f"buah[0] (pertama): {buah[0]}")
print(f"buah[1] (kedua): {buah[1]}")
print(f"buah[2] (ketiga): {buah[2]}")

# Akses dari belakang (index negatif)
print(f"\nbuah[-1] (terakhir): {buah[-1]}")
print(f"buah[-2] (kedua terakhir): {buah[-2]}")


# ============================================================
# 3. SLICING (MEMOTONG TUPLE)
# ============================================================
print("\n3. SLICING TUPLE")
print("-" * 40)

angka = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(f"Tuple asli: {angka}\n")

# tuple[start:end] - dari index start sampai sebelum end
print(f"angka[2:7] (index 2-6): {angka[2:7]}")
print(f"angka[:5] (awal sampai index 4): {angka[:5]}")
print(f"angka[5:] (index 5 sampai akhir): {angka[5:]}")
print(f"angka[::2] (lompat 2): {angka[::2]}")
print(f"angka[::-1] (reverse): {angka[::-1]}")


# ============================================================
# 4. SIFAT TUPLE TIDAK BISA DIUBAH (IMMUTABLE)
# ============================================================
print("\n4. SIFAT TUPLE BERSIFAT IMMUTABLE (TIDAK BISA DIUBAH)")
print("-" * 40)

data = (10, 20, 30, 40)
print(f"Tuple data: {data}")

# Mencoba mengubah akan ERROR
try:
    data[1] = 25  # Ini akan error!
except TypeError as e:
    print(f"ERROR: {e}")
    print("Tuple tidak bisa diubah setelah dibuat!")

# Tapi bisa dibuat tuple baru
data_baru = data + (50,)
print(f"Tuple baru dari {data} + (50,): {data_baru}")


# ============================================================
# 5. OPERASI TUPLE
# ============================================================
print("\n5. OPERASI TUPLE")
print("-" * 40)

a = (1, 2, 3)
b = (4, 5, 6)

# Penggabungan (+)
c = a + b
print(f"{a} + {b} = {c}")

# Perkalian (*)
d = a * 3
print(f"{a} * 3 = {d}")

# Pengecekan anggota (in)
print(f"2 in {a}: {2 in a}")
print(f"10 in {a}: {10 in a}")

# Panjang tuple (len)
print(f"len({a}): {len(a)}")

# Nilai terbesar & terkecil
nilai_tuple = (5, 2, 8, 1, 9)
print(f"max({nilai_tuple}): {max(nilai_tuple)}")
print(f"min({nilai_tuple}): {min(nilai_tuple)}")
print(f"sum({nilai_tuple}): {sum(nilai_tuple)}")


# ============================================================
# 6. METHOD TUPLE
# ============================================================
print("\n6. METHOD TUPLE")
print("-" * 40)

data = (3, 1, 4, 1, 5, 9, 2, 6, 5, 1)
print(f"Tuple data: {data}")

# count() - menghitung jumlah kemunculan
print(f"count(1): {data.count(1)}")
print(f"count(5): {data.count(5)}")

# index() - mencari index pertama
print(f"index(5): {data.index(5)}")
print(f"index(4): {data.index(4)}")

# Method lain seperti sort(), reverse(), append() TIDAK ADA!


# ============================================================
# 7. LOOPING PADA TUPLE
# ============================================================
print("\n7. LOOPING PADA TUPLE")
print("-" * 40)

buah = ("apel", "mangga", "jeruk", "anggur")

# Looping biasa
print("Looping dengan for:")
for item in buah:
    print(f"  - {item}")

# Looping dengan index (enumerate)
print("\nLooping dengan index:")
for i, item in enumerate(buah):
    print(f"  Index {i}: {item}")


# ============================================================
# 8. TUPLE UNPACKING
# ============================================================
print("\n8. TUPLE UNPACKING (MEMBUKA TUPLE)")
print("-" * 40)

# Unpacking ke variabel terpisah
koordinat = (10, 20)
x, y = koordinat
print(f"Tuple {koordinat} di-unpack menjadi x={x}, y={y}")

# Unpacking dengan jumlah variabel sesuai
data = ("Budi", 20, "Jakarta")
nama, umur, kota = data
print(f"Nama: {nama}, Umur: {umur}, Kota: {kota}")

# Unpacking dengan * (sisa elemen)
angka = (1, 2, 3, 4, 5)
a, b, *c = angka
print(f"a={a}, b={b}, c={c}")

# Swap variabel (tanpa variabel temporary) - menggunakan tuple
a, b = 10, 20
print(f"\nSebelum swap: a={a}, b={b}")
a, b = b, a  # swapping dengan tuple
print(f"Setelah swap: a={a}, b={b}")

# ============================================================
# 9. NESTED TUPLE (Tuple di dalam Tuple)
# ============================================================
print("\n9. TUPLE BERSARANG (NESTED TUPLE)")
print("-" * 40)

matriks = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
print("Tuple 3x3 (matriks):")
for baris in matriks:
    print(f"  {baris}")

# Mengakses elemen bertingkat
print(f"\nmatriks[0][0] (baris 1, kolom 1): {matriks[0][0]}")
print(f"matriks[1][2] (baris 2, kolom 3): {matriks[1][2]}")
print(f"matriks[2][1] (baris 3, kolom 2): {matriks[2][1]}")

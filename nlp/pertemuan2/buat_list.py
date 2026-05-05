# LIST

# ============================================================
# 1. MEMBUAT LIST (DEKLARASI & INISIALISASI)
# ============================================================
print("\n1. MEMBUAT LIST")
print("-" * 40)

# List kosong
list_kosong = []
print(f"List kosong: {list_kosong}")

# List dengan nilai
angka = [1, 2, 3, 4, 5]
print(f"List angka: {angka}")

# List dengan tipe data berbeda
campuran = [10, "Budi", 3.14, True]
print(f"List campuran: {campuran}")

# List menggunakan fungsi list()
list_dari_string = list("Python")
print(f"List dari string 'Python': {list_dari_string}")

# List dengan range()
list_range = list(range(1, 10))
print(f"List dari range(1,10): {list_range}")


# ============================================================
# 2. MENGAKSES ELEMEN LIST
# ============================================================
print("\n2. MENGAKSES ELEMEN LIST")
print("-" * 40)

buah = ["apel", "mangga", "jeruk", "anggur", "pisang"]
print(f"List buah: {buah}\n")

# Akses berdasarkan index (mulai dari 0)
print(f"buah[0] (pertama): {buah[0]}")
print(f"buah[1] (kedua): {buah[1]}")
print(f"buah[2] (ketiga): {buah[2]}")

# Akses dari belakang (index negatif)
print(f"\nbuah[-1] (terakhir): {buah[-1]}")
print(f"buah[-2] (kedua terakhir): {buah[-2]}")


# ============================================================
# 3. SLICING (MEMOTONG LIST)
# ============================================================
print("\n3. SLICING LIST")
print("-" * 40)

angka = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"List asli: {angka}\n")

# list[start:end] - dari index start sampai sebelum end
print(f"angka[2:7] (index 2-6): {angka[2:7]}")
print(f"angka[:5] (awal sampai index 4): {angka[:5]}")
print(f"angka[5:] (index 5 sampai akhir): {angka[5:]}")
print(f"angka[::2] (lompat 2): {angka[::2]}")
print(f"angka[::-1] (reverse): {angka[::-1]}")


# ============================================================
# 4. MENGUBAH ELEMEN LIST
# ============================================================
print("\n4. MENGUBAH ELEMEN LIST")
print("-" * 40)

nilai = [10, 20, 30, 40, 50]
print(f"List awal: {nilai}")

# Mengubah satu elemen
nilai[1] = 25
print(f"Setelah nilai[1] = 25: {nilai}")

# Mengubah beberapa elemen (slicing assignment)
nilai[2:4] = [100, 200]
print(f"Setelah nilai[2:4] = [100, 200]: {nilai}")


# ============================================================
# 5. MENAMBAH ELEMEN LIST
# ============================================================
print("\n5. MENAMBAH ELEMEN LIST")
print("-" * 40)

data = [1, 2, 3]
print(f"List awal: {data}")

# append() - tambah di akhir
data.append(4)
print(f"append(4): {data}")

# insert() - tambah di index tertentu
data.insert(1, 99)
print(f"insert(1, 99): {data}")

# extend() - tambah list lain
data.extend([5, 6, 7])
print(f"extend([5,6,7]): {data}")

# + operator untuk menggabung list
list_baru = data + [8, 9]
print(f"data + [8,9]: {list_baru}")


# ============================================================
# 6. MENGHAPUS ELEMEN LIST
# ============================================================
print("\n6. MENGHAPUS ELEMEN LIST")
print("-" * 40)

data = [10, 20, 30, 40, 50, 30]
print(f"List awal: {data}")

# remove() - hapus nilai pertama yang cocok
data.remove(30)
print(f"remove(30): {data}")

# pop() - hapus index tertentu (default terakhir)
hapus = data.pop()
print(f"pop() -> menghapus {hapus}, hasil: {data}")

hapus = data.pop(1)
print(f"pop(1) -> menghapus {hapus}, hasil: {data}")

# del - hapus berdasarkan index
del data[0]
print(f"del data[0]: {data}")

# clear() - hapus semua elemen
data.clear()
print(f"clear(): {data}")


# ============================================================
# 7. OPERASI LIST
# ============================================================
print("\n7. OPERASI LIST")
print("-" * 40)

a = [1, 2, 3]
b = [4, 5, 6]

# Penggabungan (+)
c = a + b
print(f"{a} + {b} = {c}")

# Perkalian (*)
d = a * 3
print(f"{a} * 3 = {d}")

# Pengecekan anggota (in)
print(f"2 in {a}: {2 in a}")
print(f"10 in {a}: {10 in a}")

# Panjang list (len)
print(f"len({a}): {len(a)}")

# Nilai terbesar & terkecil
nilai_list = [5, 2, 8, 1, 9]
print(f"max({nilai_list}): {max(nilai_list)}")
print(f"min({nilai_list}): {min(nilai_list)}")
print(f"sum({nilai_list}): {sum(nilai_list)}")


# ============================================================
# 8. METHOD LIST
# ============================================================
print("\n8. METHOD LIST")
print("-" * 40)

data = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(f"List awal: {data}")

# count() - menghitung jumlah kemunculan
print(f"count(1): {data.count(1)}")
print(f"count(5): {data.count(5)}")

# index() - mencari index pertama
print(f"index(5): {data.index(5)}")

# sort() - mengurutkan (ascending)
data.sort()
print(f"sort(): {data}")

# sort(reverse=True) - mengurutkan (descending)
data.sort(reverse=True)
print(f"sort(reverse=True): {data}")

# reverse() - membalik urutan
data.reverse()
print(f"reverse(): {data}")

# copy() - membuat salinan list
data_copy = data.copy()
print(f"copy(): {data_copy}")


# ============================================================
# 9. LOOPING PADA LIST
# ============================================================
print("\n9. LOOPING PADA LIST")
print("-" * 40)

buah = ["apel", "mangga", "jeruk", "anggur"]

# Looping biasa
print("Looping dengan for:")
for item in buah:
    print(f"  - {item}")

# Looping dengan index (enumerate)
print("\nLooping dengan index:")
for i, item in enumerate(buah):
    print(f"  Index {i}: {item}")

# Looping dengan range
print("\nLooping dengan range(len()):")
for i in range(len(buah)):
    print(f"  {buah[i]}")

# ============================================================
# 10. LIST MULTIDIMENSI (List di dalam List)
# ============================================================
print("\n10. LIST MULTIDIMENSI")
print("-" * 40)

# Matriks 3x3
matriks = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Matriks 3x3:")
for baris in matriks:
    print(f"  {baris}")

# Mengakses elemen
print(f"\nmatriks[0][0] (baris 1, kolom 1): {matriks[0][0]}")
print(f"matriks[1][2] (baris 2, kolom 3): {matriks[1][2]}")
print(f"matriks[2][1] (baris 3, kolom 2): {matriks[2][1]}")

# Mengubah elemen
matriks[1][1] = 99
print(f"\nSetelah ubah matriks[1][1] = 99:")
for baris in matriks:
    print(f"  {baris}")

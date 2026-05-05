# PYTHON KEYWORDS

# ============================================================
# 1. VALUE KEYWORDS (Boolean & None)
# ============================================================
print("=" * 50)
print("1. VALUE KEYWORDS: True, False, None")
print("=" * 50)

is_active = True      # Keyword: True
is_closed = False     # Keyword: False
data = None           # Keyword: None

print(f"is_active: {is_active}")
print(f"is_closed: {is_closed}")
print(f"data: {data}\n")


# ============================================================
# 2. LOGICAL OPERATORS (and, or, not)
# ============================================================
print("=" * 50)
print("2. LOGICAL OPERATORS: and, or, not")
print("=" * 50)

x = 10
y = 5

# Keyword: and
if x > 5 and y > 0:
    print("and: x > 5 DAN y > 0 bernilai True")

# Keyword: or
if x > 100 or y > 0:
    print("or: x > 100 atau y > 0 bernilai True")

# Keyword: not
if not x == 100:
    print(f"not: x ({x}) tidak sama dengan 100\n")


# ============================================================
# 3. CONDITIONAL KEYWORDS (if, elif, else)
# ============================================================
print("=" * 50)
print("3. CONDITIONAL: if, elif, else")
print("=" * 50)

nilai = 85

# Keyword: if
if nilai >= 90:
    predikat = "A"
# Keyword: elif
elif nilai >= 75:
    predikat = "B"
# Keyword: else
else:
    predikat = "C"

print(f"Nilai {nilai} mendapatkan predikat {predikat}\n")


# ============================================================
# 4. LOOPING KEYWORDS (for, while, break, continue, else)
# ============================================================
print("=" * 50)
print("4. LOOPING: for, while, break, continue, else")
print("=" * 50)

# Keyword: for, in
print("for loop dengan break:")
for i in range(1, 6):
    if i == 3:
        break  # Keyword: break - menghentikan loop
    print(f"  i = {i}")

# Keyword: continue
print("\nwhile loop dengan continue:")
angka = 0
while angka < 5:  # Keyword: while
    angka += 1
    if angka == 3:
        continue  # Keyword: continue - loncat ke iterasi berikutnya
    print(f"  angka = {angka}")

# Keyword: else pada loop (dieksekusi jika loop selesai tanpa break)
print("\nfor loop dengan else:")
for j in range(1, 4):
    print(f"  j = {j}")
else:  # Keyword: else untuk loop
    print("  Loop selesai tanpa break!\n")


# ============================================================
# 5. FUNCTION KEYWORDS (def, return, lambda, pass, yield)
# ============================================================
print("=" * 50)
print("5. FUNCTION: def, return, lambda, pass, yield")
print("=" * 50)

# Keyword: def - mendefinisikan fungsi
def tambah(a, b):
    # Keyword: return - mengembalikan nilai
    return a + b

# Keyword: lambda - fungsi anonim
kali = lambda x, y: x * y

# Keyword: pass - tidak melakukan apa-apa (placeholder)
def fungsi_kosong():
    pass  # nanti akan diisi

# Keyword: yield - generator function
def angka_genap(n):
    for i in range(0, n+1, 2):
        yield i  # menghasilkan nilai satu per satu

print(f"tambah(10, 5) = {tambah(10, 5)}")
print(f"kali(4, 3) = {kali(4, 3)}")

print("Generator dengan yield:")
for genap in angka_genap(6):
    print(f"  {genap}", end=" ")
print("\n")


# ============================================================
# 6. CLASS & OBJECT KEYWORDS (class, def, is, as)
# ============================================================
print("=" * 50)
print("6. CLASS: class, def, is, as")
print("=" * 50)

# Keyword: class - mendefinisikan class
class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
    
    def perkenalan(self):
        return(f"Halo, saya {self.nama} dengan NIM {self.nim}")

# Keyword: as - alias / digunakan dengan with
import math as mt  # as: memberi alias

# Keyword: is - membandingkan identitas objek
mhs1 = Mahasiswa("Budi", "12345")
mhs2 = Mahasiswa("Budi", "12345")
mhs3 = mhs1

print(mhs1.perkenalan())
print(f"mhs1 is mhs3: {mhs1 is mhs3}")     # True (objek sama)
print(f"mhs1 is mhs2: {mhs1 is mhs2}")     # False (objek berbeda)
print(f"Nilai pi: {mt.pi}\n")              # menggunakan alias as


# ============================================================
# 7. EXCEPTION HANDLING (try, except, finally, raise, assert)
# ============================================================
print("=" * 50)
print("7. EXCEPTION: try, except, finally, raise, assert")
print("=" * 50)

# Keyword: try, except, finally
def bagi_angka(a, b):
    try:
        hasil = a / b
    except ZeroDivisionError as e:  # Keyword: except
        print(f"Error: {e}")
        raise ValueError("Tidak bisa membagi dengan nol!")  # Keyword: raise
    else:  # Keyword: else untuk try-except
        return hasil
    finally:  # Keyword: finally - selalu dieksekusi
        print("  (Block finally selesai dieksekusi)")

# Keyword: assert - untuk debugging
def cek_usia(usia):
    assert usia >= 18, "Usia harus minimal 18 tahun!"  # assert
    return "Akses diberikan"

print("Hasil bagi 10/2:", bagi_angka(10, 2))
print("Hasil cek_usia(20):", cek_usia(20))

try:
    print("\nMencoba bagi 10/0:")
    bagi_angka(10, 0)
except ValueError as e:
    print(f"  Terjadi error: {e}")

try:
    print("\nMencoba cek_usia(15):")
    cek_usia(15)
except AssertionError as e:
    print(f"  AssertionError: {e}\n")


# ============================================================
# 8. IMPORT & VARIABLE KEYWORDS (import, from, global, nonlocal)
# ============================================================
print("=" * 50)
print("8. IMPORT & VARIABLE: import, from, global, nonlocal")
print("=" * 50)

# Keyword: from
from datetime import datetime

# Keyword: global
counter = 0

def increment():
    global counter  # menggunakan variabel global
    counter += 1

# Keyword: nonlocal (untuk nested function)
def outer():
    x = 10
    def inner():
        nonlocal x  # mengakses variabel dari outer scope
        x = 20
    inner()
    return x

increment()
increment()
print(f"global counter: {counter}")
print(f"nonlocal example: outer() = {outer()}")
print(f"Waktu sekarang: {datetime.now().strftime('%H:%M:%S')}\n")


# ============================================================
# 9. ASYNC KEYWORDS (async, await)
# ============================================================
print("=" * 50)
print("9. ASYNC: async, await")
print("=" * 50)

import asyncio

# Keyword: async - mendefinisikan fungsi async
async def proses_data(nama):
    print(f"Memulai proses {nama}...")
    await asyncio.sleep(1)  # Keyword: await - menunggu async operation
    print(f"Proses {nama} selesai!")
    return f"Hasil dari {nama}"

async def main():
    # Menjalankan multiple async tasks
    tasks = [proses_data("A"), proses_data("B")]
    results = await asyncio.gather(*tasks)
    print(f"Hasil: {results}")

# Menjalankan async function
# asyncio.run(main())  # Uncomment untuk menjalankan

print("Async functions sudah didefinisikan (contoh async/await)\n")


# ============================================================
# 10. LAINNYA (del, with, in)
# ============================================================
print("=" * 50)
print("10. LAINNYA: del, with, in")
print("=" * 50)

# Keyword: del - menghapus variabel/atribut
daftar = [1, 2, 3, 4, 5]
print(f"Sebelum del: {daftar}")
del daftar[2]  # menghapus index ke-2
print(f"Setelah del index ke-2: {daftar}")

# Keyword: with - context manager
with open("contoh.txt", "w") as file:  # with - otomatis menutup file
    file.write("Ini contoh penggunaan keyword 'with'")

# Keyword: in - pengecekan keanggotaan
buah = ["apel", "mangga", "jeruk"]
if "mangga" in buah:
    print("Mangga ada dalam daftar buah!")


# ============================================================
# LIST SEMUA KEYWORDS
# ============================================================
print("\n" + "=" * 50)
print("DAFTAR SEMUA 35 PYTHON KEYWORDS")
print("=" * 50)

keywords_list = [
    "False", "None", "True", "and", "as", "assert", "async", "await",
    "break", "class", "continue", "def", "del", "elif", "else", "except",
    "finally", "for", "from", "global", "if", "import", "in", "is",
    "lambda", "nonlocal", "not", "or", "pass", "raise", "return",
    "try", "while", "with", "yield"
]

# Menampilkan dalam format grid
for i, kw in enumerate(keywords_list, 1):
    print(f"{i:2}. {kw}", end="   ")
    if i % 5 == 0:
        print()
print("\n")

print("Total keywords: 35")
print("Program selesai!")
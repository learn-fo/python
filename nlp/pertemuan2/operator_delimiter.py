# OPERATOR DAN DELIMITER

# ============================================================
# DELIMITER (Kurung dan Pemisah)
# ============================================================
print("\n1. DELIMITER")

# ( ) - Kurung
print("\n--- ( ) ---")
def kali_dua(x):
    return x * 2
print(f"kali_dua(5) = {kali_dua(5)}")
print(f"Tuple: {(1, 2, 3)}")

# [ ] - Kurung siku
print("\n--- [ ] ---")
list_angka = [1, 2, 3, 4]
print(f"List: {list_angka}")
print(f"Index ke-0: {list_angka[0]}")
print(f"Slicing [1:3]: {list_angka[1:3]}")

# { } - Kurung kurawal
print("\n--- { } ---")
data = {"nama": "Budi", "umur": 20}
print(f"Dictionary: {data}")
print(f"Set: {1, 2, 3, 2, 1}")

# , - Koma
print("\n--- , ---")
a, b = 5, 10
print(f"a,b = {a},{b}")

# : - Colon
print("\n--- : ---")
teks = "Python"
print(f"teks[:3]: {teks[:3]}")
print(f"teks[3:]: {teks[3:]}")

# . - Titik
print("\n--- . ---")
print(f"teks.upper(): {teks.upper()}")

# ; - Semicolon
print("\n--- ; ---")
x = 1; y = 2; print(f"x={x}, y={y}")

# @ - At (decorator)
print("\n--- @ ---")
def sederhana(func):
    return func

@sederhana
def halo():
    return "Halo!"

print(f"@decorator: {halo()}")

# = - Assignment
print("\n--- = ---")
nama = "Siti"
print(f"nama = {nama}")

# -> - Arrow
print("\n--- -> ---")
def panggil(nama: str) -> str:
    return f"Halo {nama}"
print(panggil("Ali"))


# ============================================================
# OPERATOR ARITMATIKA
# ============================================================
print("\n" + "=" * 60)
print("2. OPERATOR ARITMATIKA")
print("=" * 60)

a, b = 10, 3
print(f"a = {a}, b = {b}\n")

print(f"a + b = {a + b}   # Penjumlahan")
print(f"a - b = {a - b}   # Pengurangan")
print(f"a * b = {a * b}   # Perkalian")
print(f"a ** b = {a ** b} # Pangkat (10^3)")
print(f"a / b = {a / b}   # Pembagian (float)")
print(f"a // b = {a // b} # Pembagian bulat")
print(f"a % b = {a % b}   # Sisa bagi")

# @ untuk matriks
print(f"\nMatrix @ (Python 3.5+):")
import numpy as np
A = [[1,2],[3,4]]
B = [[5,6],[7,8]]
print(f"Tidak perlu numpy, gunakan np.array(A) @ np.array(B)")


# ============================================================
# OPERATOR BITWISE
# ============================================================
print("\n" + "=" * 60)
print("3. OPERATOR BITWISE")
print("=" * 60)

x, y = 6, 3  # 6=110, 3=011
print(f"x = {x} (biner: {bin(x)[2:]})")
print(f"y = {y} (biner: {bin(y)[2:]})\n")

print(f"x & y = {x & y}   # AND (110 & 011 = 010 = 2)")
print(f"x | y = {x | y}   # OR  (110 | 011 = 111 = 7)")
print(f"x ^ y = {x ^ y}   # XOR (110 ^ 011 = 101 = 5)")
print(f"~x = {~x}         # NOT (komplemen)")
print(f"x << 1 = {x << 1} # Geser kiri 1 bit (6*2=12)")
print(f"x >> 1 = {x >> 1} # Geser kanan 1 bit (6/2=3)")


# ============================================================
# OPERATOR PERBANDINGAN
# ============================================================
print("\n" + "=" * 60)
print("4. OPERATOR PERBANDINGAN")
print("=" * 60)

p, q = 10, 5
print(f"p = {p}, q = {q}\n")

print(f"p < q  = {p < q}   # Kurang dari")
print(f"p > q  = {p > q}   # Lebih dari")
print(f"p <= q = {p <= q}  # Kurang/sama dengan")
print(f"p >= q = {p >= q}  # Lebih/sama dengan")
print(f"p == q = {p == q}  # Sama dengan")
print(f"p != q = {p != q}  # Tidak sama dengan")


# ============================================================
# WALRUS OPERATOR (:=)
# ============================================================
print("\n" + "=" * 60)
print("5. WALRUS OPERATOR (:=) - Python 3.8+")
print("=" * 60)

# Contoh: assignment dalam if
data = [1, 2, 3, 4, 5]
if (panjang := len(data)) > 3:
    print(f"Data panjangnya {panjang}, lebih dari 3")

# Contoh: dalam while
i = 0
while (nilai := i + 1) <= 3:
    print(f"  nilai ke-{nilai}")
    i = nilai

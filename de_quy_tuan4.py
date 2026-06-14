# Assignment Tuan 4: Lam tren lop ngay 10/06/2026
# SINH VIEN LAM CAC BAI TAP SAU BANG DE QUY

# Bai 1: Tinh tong S(n) = 1+2+3+...+n bang de quy
print("=== Bai 1 ===")
def tong(n):
    if n == 1:
        return 1
    return n + tong(n - 1)

n = int(input("Nhap so nguyen n: "))
print(f"S({n}) = {tong(n)}")

# Bai 2: Tinh n! bang de quy
print("\n=== Bai 2 ===")
def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    return n * giai_thua(n - 1)

n = int(input("Nhap so nguyen n: "))
print(f"{n}! = {giai_thua(n)}")

# Bai 3: Tinh a^n bang de quy
print("\n=== Bai 3 ===")
def luy_thua(a, n):
    if n == 0:
        return 1
    return a * luy_thua(a, n - 1)

a = int(input("Nhap co so a: "))
n = int(input("Nhap so mu n: "))
print(f"{a}^{n} = {luy_thua(a, n)}")

# Bai 4: Tinh tong S(n) = 1 + 1/2 + 1/3 + ... + 1/n bang de quy
print("\n=== Bai 4 ===")
def tong_1_n(n):
    if n == 1:
        return 1.0
    return 1/n + tong_1_n(n - 1)

n = int(input("Nhap so nguyen n: "))
print(f"S({n}) = 1 + 1/2 + ... + 1/{n} = {tong_1_n(n):.6f}")

# Bai 5: Tinh tong S(n) = 1^2 + 2^2 + 3^2 + ... + n^2 bang de quy
print("\n=== Bai 5 ===")
def tong_binh_phuong(n):
    if n == 1:
        return 1
    return n**2 + tong_binh_phuong(n - 1)

n = int(input("Nhap so nguyen n: "))
print(f"S({n}) = 1^2 + 2^2 + ... + {n}^2 = {tong_binh_phuong(n)}")

# Bai 6: Tinh tong S(n) = 1/1^2 + 1/2^2 + 1/3^2 + ... + 1/n^2 bang de quy
print("\n=== Bai 6 ===")
def tong_1_binh_phuong(n):
    if n == 1:
        return 1.0
    return 1/(n**2) + tong_1_binh_phuong(n - 1)

n = int(input("Nhap so nguyen n: "))
print(f"S({n}) = 1/1^2 + 1/2^2 + ... + 1/{n}^2 = {tong_1_binh_phuong(n):.6f}")

# Bai 7: Tim so Fibonacci thu n bang de quy
print("\n=== Bai 7 ===")
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Nhap vi tri n trong day Fibonacci: "))
print(f"So Fibonacci thu {n} = {fibonacci(n)}")

# Bai 8: Dem so chu so cua mot so nguyen n bang de quy
print("\n=== Bai 8 ===")
def dem_chu_so(n):
    n = abs(n)
    if n < 10:
        return 1
    return 1 + dem_chu_so(n // 10)

n = int(input("Nhap so nguyen n: "))
print(f"So {n} co {dem_chu_so(n)} chu so")

# Bai 9: Dem so chu so chan cua mot so nguyen n bang de quy
print("\n=== Bai 9 ===")
def dem_chu_so_chan(n):
    n = abs(n)
    chu_so = n % 10
    dem = 1 if chu_so % 2 == 0 else 0
    if n < 10:
        return dem
    return dem + dem_chu_so_chan(n // 10)

n = int(input("Nhap so nguyen n: "))
print(f"So {n} co {dem_chu_so_chan(n)} chu so chan")

# Bai 10: Tinh tong cac chu so cua mot so nguyen n bang de quy
print("\n=== Bai 10 ===")
def tong_chu_so(n):
    n = abs(n)
    if n < 10:
        return n
    return n % 10 + tong_chu_so(n // 10)

n = int(input("Nhap so nguyen n: "))
print(f"Tong cac chu so cua {n} = {tong_chu_so(n)}")

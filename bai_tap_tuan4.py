# Assignment Tuan 4: Bai tap luyen tap o nha

# Bai tap 1: Kiem tra so duong, am hay bang khong
print("=== Bai 1 ===")
n = int(input("Nhap mot so nguyen: "))
if n > 0:
    print("So duong")
elif n < 0:
    print("So am")
else:
    print("Bang khong")

# Bai tap 2: In cac so tu 1 den 10
print("\n=== Bai 2 ===")
for i in range(1, 11):
    print(i)

# Bai tap 3: Tinh tong tu 1 den n
print("\n=== Bai 3 ===")
n = int(input("Nhap so nguyen duong n: "))
tong = sum(range(1, n + 1))
print(f"Tong tu 1 den {n} = {tong}")

# Bai tap 4: Kiem tra so chan hay le
print("\n=== Bai 4 ===")
n = int(input("Nhap mot so nguyen: "))
if n % 2 == 0:
    print(f"{n} la so chan")
else:
    print(f"{n} la so le")

# Bai tap 5: In cac so chan tu 2 den 20
print("\n=== Bai 5 ===")
for i in range(2, 21, 2):
    print(i, end=" ")
print()

# Bai tap 6: Dem so chu so cua mot so nguyen duong
print("\n=== Bai 6 ===")
n = int(input("Nhap mot so nguyen duong: "))
print(f"So {n} co {len(str(abs(n)))} chu so")

# Bai tap 7: Tinh n! bang vong lap
print("\n=== Bai 7 ===")
n = int(input("Nhap so nguyen n: "))
giai_thua = 1
for i in range(1, n + 1):
    giai_thua *= i
print(f"{n}! = {giai_thua}")

# Bai tap 8: Bang cuu chuong
print("\n=== Bai 8 ===")
n = int(input("Nhap so tu 1 den 9: "))
for i in range(1, 10):
    print(f"{n} x {i} = {n * i}")

# Bai tap 9: In so tu 1 den 100, bo qua so chia het cho 3
print("\n=== Bai 9 ===")
for i in range(1, 101):
    if i % 3 != 0:
        print(i, end=" ")
print()

# Bai tap 10: Tim so nguyen dau tien lon hon 100 va chia het cho 7
print("\n=== Bai 10 ===")
n = 101
while n % 7 != 0:
    n += 1
print(f"So nguyen dau tien lon hon 100 va chia het cho 7: {n}")

# Bai tap 11: Kiem tra so nguyen to
print("\n=== Bai 11 ===")
n = int(input("Nhap mot so duong: "))
la_nguyen_to = n > 1
for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        la_nguyen_to = False
        break
print(f"{n} {'la' if la_nguyen_to else 'khong la'} so nguyen to")

# Bai tap 12: In n so dau tien trong day Fibonacci
print("\n=== Bai 12 ===")
n = int(input("Nhap so nguyen n: "))
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()

# Bai tap 13: Tinh tong cac chu so
print("\n=== Bai 13 ===")
n = int(input("Nhap mot so: "))
tong = sum(int(c) for c in str(abs(n)))
print(f"Tong cac chu so cua {n} = {tong}")

# Bai tap 14: Dem ky tu trong chuoi
print("\n=== Bai 14 ===")
chuoi = input("Nhap mot chuoi: ")
ky_tu = input("Nhap ky tu can dem: ")
print(f"Ky tu '{ky_tu}' xuat hien {chuoi.count(ky_tu)} lan trong chuoi")

# Bai tap 15: Giai thua bang de quy
print("\n=== Bai 15 ===")
def giai_thua_dq(n):
    if n == 0 or n == 1:
        return 1
    return n * giai_thua_dq(n - 1)

n = int(input("Nhap so nguyen n: "))
print(f"{n}! = {giai_thua_dq(n)}")

# Bai tap 16: Tinh GCD bang vong lap
print("\n=== Bai 16 ===")
a = int(input("Nhap so nguyen duong a: "))
b = int(input("Nhap so nguyen duong b: "))
x, y = a, b
while y != 0:
    x, y = y, x % y
print(f"UCLN({a}, {b}) = {x}")

# Bai tap 17: Tim cac so hoan hao tu 1 den 1000
print("\n=== Bai 17 ===")
print("Cac so hoan hao tu 1 den 1000:")
for n in range(1, 1001):
    tong_uoc = sum(i for i in range(1, n) if n % i == 0)
    if tong_uoc == n:
        print(n, end=" ")
print()

# Bai tap 18: Dao nguoc cac chu so
print("\n=== Bai 18 ===")
n = int(input("Nhap mot so duong: "))
print(f"Dao nguoc: {str(n)[::-1]}")

# Bai tap 19: Tim chu so lon nhat trong so
print("\n=== Bai 19 ===")
n = int(input("Nhap mot so nguyen duong: "))
print(f"Chu so lon nhat trong {n}: {max(str(n))}")

# Bai tap 20: Tinh tong 1 den n bang de quy
print("\n=== Bai 20 ===")
def tong_de_quy(n):
    if n == 1:
        return 1
    return n + tong_de_quy(n - 1)

n = int(input("Nhap so nguyen n: "))
print(f"Tong tu 1 den {n} = {tong_de_quy(n)}")

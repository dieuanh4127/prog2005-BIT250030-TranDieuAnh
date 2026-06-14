# Assignment: Vong lap For tren lop ngay 01/06/2026

# Bai 1: In cac so trong doan tu 0 toi n-1
print("=== Bai 1 ===")
n = int(input("Nhap so nguyen n: "))
for i in range(0, n):
    print(i, end=" ")
print()

# Bai 2: In cac so trong doan tu 0 toi n
print("\n=== Bai 2 ===")
n = int(input("Nhap so nguyen n: "))
for i in range(0, n + 1):
    print(i, end=" ")
print()

# Bai 3: In cac so chan trong doan tu 4 toi n
print("\n=== Bai 3 ===")
n = int(input("Nhap so nguyen n: "))
for i in range(4, n + 1):
    if i % 2 == 0:
        print(i, end=" ")
print()

# Bai 4: In cac so chia het cho 5 trong doan tu 10 toi n
print("\n=== Bai 4 ===")
n = int(input("Nhap so nguyen n: "))
for i in range(10, n + 1):
    if i % 5 == 0:
        print(i, end=" ")
print()

# Bai 5: In cac so khong chia het cho 3 trong doan tu 10 toi n
print("\n=== Bai 5 ===")
n = int(input("Nhap so nguyen n: "))
for i in range(10, n + 1):
    if i % 3 != 0:
        print(i, end=" ")
print()

# Bai 6: Tinh va in ra tong S(n) = 1+2+3+...+n
print("\n=== Bai 6 ===")
n = int(input("Nhap so nguyen n: "))
tong = 0
for i in range(1, n + 1):
    tong += i
print(f"S({n}) = 1+2+3+...+{n} = {tong}")

# Bai 7: Tinh va in ra n!
print("\n=== Bai 7 ===")
n = int(input("Nhap so nguyen n: "))
giai_thua = 1
for i in range(1, n + 1):
    giai_thua *= i
print(f"{n}! = {giai_thua}")


n = int(input("Nhập n: "))

print("\nHình 1: Ma trận số 1")
for i in range(n):
    print("1 " * n)

print("\nHình 2: Ma trận số tăng theo cột")
for i in range(n):
    for j in range(1, n+1):
        print(j, end=" ")
    print()

print("\nHình 3: Tam giác số tăng dần")
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

print("\nHình 4: Tam giác số ngược")
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

print("\nHình 5: Hình bậc thang số")
for i in range(1, n+1):
    for j in range(1, n+1):
        if j <= i:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()

print("\nHình 6: Tam giác số phải xuống trái")
for i in range(n, 0, -1):
    print("   " * (n - i), end="")
    for j in range(1, i+1):
        print(j, end=" ")
    print()

print("\nHình 7: Hình thoi số đặc")
for i in range(1, n+1):
    print("   " * (n - i), end="")
    for j in range(1, i+1):
        print(i, end="   ")
    print()
for i in range(n-1, 0, -1):
    print("   " * (n - i), end="")
    for j in range(1, i+1):
        print(i, end="   ")
    print()

print("\nHình 8: Hình đồng hồ cát số")
for i in range(1, 2*n):
    for j in range(1, 2*n):
        if j <= i and j <= 2*n - i:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()

print("\nHình 9: Hình X số")
for i in range(1, n+1):
    for j in range(1, n+1):
        if j == i or j == n - i + 1:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()



n = int(input("Nhập n: "))

print("\nHình 1: Tam giác số tăng dần")
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

print("\nHình 2: Tam giác số ngược")
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

print("\nHình 3: Tam giác số phải")
for i in range(1, n+1):
    print("  " * (n - i), end="")
    for j in range(1, i+1):
        print(j, end=" ")
    print()

print("\nHình 4: Hình thoi sao")
for i in range(1, n+1):
    print("  " * (n - i) + "* " * i)
for i in range(n-1, 0, -1):
    print("  " * (n - i) + "* " * i)

print("\nHình 5: Hình thoi số")
for i in range(1, n+1):
    print("  " * (n - i), end="")
    for j in range(1, i+1):
        print(j, end=" ")
    print()
for i in range(n-1, 0, -1):
    print("  " * (n - i), end="")
    for j in range(1, i+1):
        print(j, end=" ")
    print()

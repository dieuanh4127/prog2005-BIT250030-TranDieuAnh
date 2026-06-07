
n = int(input("Nhập n: "))

print("\nHình 1: Tam giác vuông trái (tăng dần)")
for i in range(1, n+1):
    print("* " * i)

print("\nHình 2: Tam giác vuông trái (giảm dần)")
for i in range(n, 0, -1):
    print("* " * i)

print("\nHình 3: Tam giác vuông phải (tăng dần)")
for i in range(1, n+1):
    print("  " * (n - i) + "* " * i)

print("\nHình 4: Tam giác ngược phải (giảm dần)")
for i in range(n, 0, -1):
    print("  " * (n - i) + "* " * i)

print("\nHình 5: Tam giác cân (sao hai bên, tăng)")
for i in range(1, n+1):
    spaces = "  " * (n - i)
    if i == 1:
        stars = "*"
    else:
        stars = "* " + "  " * (i - 2) + "*"
    print(spaces + stars)

print("\nHình 6: Tam giác ngược (sao hai bên, giảm)")
for i in range(n, 0, -1):
    spaces = "  " * (n - i)
    if i == 1:
        stars = "*"
    else:
        stars = "* " + "  " * (i - 2) + "*"
    print(spaces + stars)

print("\nHình 7: Tam giác cân đặc (tăng)")
for i in range(1, n+1):
    print("  " * (n - i) + "* " * i)

print("\nHình 8: Tam giác cân đặc (giảm)")
for i in range(n, 0, -1):
    print("  " * (n - i) + "* " * i)

print("\nHình 9: Hình thoi rỗng")
for i in range(1, n+1):
    spaces = "  " * (n - i)
    if i == 1:
        stars = "*"
    else:
        stars = "* " + "  " * (i - 2) + "*"
    print(spaces + stars)
for i in range(n-1, 0, -1):
    spaces = "  " * (n - i)
    if i == 1:
        stars = "*"
    else:
        stars = "* " + "  " * (i - 2) + "*"
    print(spaces + stars)

print("\nHình 10: Hình X")
for i in range(1, n+1):
    row = ""
    for j in range(1, n+1):
        if j == i or j == n - i + 1:
            row += "* "
        else:
            row += "  "
    print(row)

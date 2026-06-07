

n = int(input("Nhập n: "))
size = 2 * n - 1
print()
for i in range(1, size + 1):
    for j in range(1, size + 1):
        if (i + j == n + 1) or (i - j == n - 1) or \
           (j - i == n - 1) or (i + j == 3 * n - 1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()



m = int(input("Nhập m (số hàng): "))
n = int(input("Nhập n (số cột): "))
print()
for i in range(m):
    row = ""
    for j in range(n):
        row += "*   "
    print(row)

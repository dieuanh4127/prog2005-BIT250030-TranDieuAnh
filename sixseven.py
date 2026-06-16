# ===== BAI 1 =====
# In moi phan tu tren 1 dong
def bai1():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    for x in arr:
        print(x)


# ===== BAI 2 =====
# In theo dinh dang arr[i]=...
def bai2():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    for i in range(n):
        print(f"arr[{i}]={arr[i]}")


# ===== BAI 3 =====
# In nguoc tu cuoi len dau
def bai3():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    parts = [f"arr[{i}]={arr[i]}" for i in range(n-1, -1, -1)]
    print(", ".join(parts))


# ===== BAI 4 =====
# In cac phan tu co index la so chan
def bai4():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    for i in range(n):
        if i % 2 == 0:
            print(arr[i])


# ===== BAI 5 =====
# In cac phan tu co gia tri la so chan
def bai5():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    for x in arr:
        if x % 2 == 0:
            print(x)


# ===== BAI 6 =====
# Tinh tong tat ca phan tu
def bai6():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    print(sum(arr))


# ===== BAI 7 =====
# Tim so nguyen to kem vi tri
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def bai7():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    for i in range(n):
        if is_prime(arr[i]):
            print(f"arr[{i}]={arr[i]}")


# ===== MAIN =====
if __name__ == "__main__":
    print("Chon bai (1-7): ", end="")
    choice = int(input())
    funcs = {1: bai1, 2: bai2, 3: bai3, 4: bai4, 5: bai5, 6: bai6, 7: bai7}
    if choice in funcs:
        funcs[choice]()
    else:
        print("Bai khong hop le!")
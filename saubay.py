# ============================================================
# BÀI 1: Kiểm tra số chẵn
# ============================================================

# Tạo một hàm tên là is_even, nhận vào một số nguyên n
def is_even(n):
    # Dùng % (phép chia lấy phần dư) để kiểm tra
    # Nếu n chia 2 dư 0 → số chẵn → trả về True
    # Ngược lại → số lẻ → trả về False
    if n % 2 == 0:
        return True
    else:
        return False

# Gọi thử hàm và in kết quả ra màn hình
print(is_even(4))   # Kết quả: True  (vì 4 chia 2 dư 0)
print(is_even(7))   # Kết quả: False (vì 7 chia 2 dư 1)


# ============================================================
# BÀI 2: Tìm số lớn nhất trong 3 số
# ============================================================

# Nhập 3 số từ bàn phím, int() để chuyển chữ thành số nguyên
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
c = int(input("Nhập số thứ ba: "))

# Dùng hàm max() có sẵn của Python để tìm số lớn nhất
# Truyền cả 3 số vào, Python tự so sánh và trả về cái lớn nhất
lon_nhat = max(a, b, c)

# In kết quả ra màn hình
print("Số lớn nhất là:", lon_nhat)


# ============================================================
# BÀI 3: Hàm với đối số mặc định
# ============================================================

# Tạo hàm greet với tham số name có giá trị mặc định là "Student"
# Nếu gọi hàm mà không truyền tên → tự dùng "Student"
def greet(name="Student"):
    print("Hello,", name + "!")

# Gọi hàm CÓ truyền tên → dùng tên mình truyền vào
greet("An")       # Kết quả: Hello, An!

# Gọi hàm KHÔNG truyền tên → tự dùng "Student" (giá trị mặc định)
greet()           # Kết quả: Hello, Student!


# ============================================================
# BÀI 4: Kiểm tra đầu vào tuổi
# ============================================================

# Nhập tuổi từ bàn phím và chuyển thành số nguyên
tuoi = int(input("Nhập tuổi của bạn: "))

# Kiểm tra xem tuổi có nằm trong khoảng hợp lệ không (1 đến 120)
if 1 <= tuoi <= 120:
    # Tuổi hợp lệ → in thông báo bình thường
    print("Tuổi hợp lệ:", tuoi)
else:
    # Tuổi không hợp lệ (âm, bằng 0, hoặc quá 120) → báo lỗi
    print("Tuổi không hợp lệ! Vui lòng nhập từ 1 đến 120.")


# ============================================================
# BÀI 5: Đếm số lần xuất hiện ký tự 'a'
# ============================================================

# Nhập một chuỗi ký tự từ bàn phím
chuoi = input("Nhập một chuỗi: ")

# Dùng phương thức .count() có sẵn để đếm
# .count('a') → đếm xem chữ 'a' xuất hiện bao nhiêu lần trong chuỗi
so_lan = chuoi.count('a')

# In kết quả ra màn hình
print("Chữ 'a' xuất hiện", so_lan, "lần")


# ============================================================
# BÀI 6: Chuyển độ C sang độ F
# ============================================================

# Nhập nhiệt độ dạng số thực (float), ví dụ: 36.5
celsius = float(input("Nhập nhiệt độ (°C): "))

# Áp dụng công thức chuyển đổi: F = C × 9/5 + 32
fahrenheit = celsius * 9 / 5 + 32

# In kết quả theo dạng chuỗi định dạng f-string
# :.2f → làm tròn 2 chữ số thập phân
print(f"{celsius}°C = {fahrenheit:.2f}°F")


# ============================================================
# BÀI 7: Tính BMI (Chỉ số khối cơ thể)
# ============================================================

# Nhập cân nặng (kg) và chiều cao (m) dạng số thực
weight = float(input("Nhập cân nặng (kg): "))
height = float(input("Nhập chiều cao (m): "))

# Tính BMI theo công thức: cân nặng chia cho bình phương chiều cao
# height ** 2 là height × height (lũy thừa bậc 2)
bmi = weight / (height ** 2)

# In kết quả, :.2f giúp làm tròn còn 2 chữ số sau dấu phẩy
print(f"Chỉ số BMI của bạn là: {bmi:.2f}")


# ============================================================
# BÀI 8: Phép chia — xử lý lỗi chia cho 0 và dữ liệu không hợp lệ
# ============================================================

# try...except dùng để "thử" chạy code, nếu lỗi thì xử lý thay vì crash
try:
    # Nhập 2 số nguyên từ bàn phím
    a = int(input("Nhập số bị chia: "))
    b = int(input("Nhập số chia: "))

    # Thực hiện phép chia
    ket_qua = a / b
    print(f"Kết quả: {a} / {b} = {ket_qua}")

except ZeroDivisionError:
    # Bắt lỗi chia cho 0 (Python không cho chia cho 0)
    print("Lỗi: Không thể chia cho 0!")

except ValueError:
    # Bắt lỗi khi người dùng nhập chữ thay vì số
    print("Lỗi: Vui lòng nhập số nguyên hợp lệ!")


# ============================================================
# BÀI 9: Tính căn bậc hai
# ============================================================

# Import thư viện math để dùng hàm sqrt() (căn bậc hai)
import math

# Nhập một số từ bàn phím dạng số thực
so = float(input("Nhập một số: "))

# Kiểm tra: số âm không có căn bậc hai thực → báo lỗi
if so < 0:
    print("Lỗi: Không thể tính căn bậc hai của số âm!")
else:
    # math.sqrt() tính căn bậc hai, ví dụ sqrt(9) = 3.0
    can = math.sqrt(so)
    print(f"Căn bậc hai của {so} là: {can:.2f}")


# ============================================================
# BÀI 10: Nhập thông tin 3 sinh viên và tính điểm trung bình
# ============================================================

# Dùng vòng lặp for để lặp 3 lần (cho 3 sinh viên)
# range(3) tạo ra dãy số 0, 1, 2 → lặp đúng 3 lần
for i in range(3):
    print(f"\n--- Sinh viên thứ {i + 1} ---")

    # Nhập tên sinh viên (để nguyên dạng chuỗi, không cần int/float)
    ten = input("Tên sinh viên: ")

    # Nhập điểm 3 môn, chuyển sang số thực để tính trung bình
    toan = float(input("Điểm Toán: "))
    ly   = float(input("Điểm Lý: "))
    hoa  = float(input("Điểm Hóa: "))

    # Tính điểm trung bình: cộng 3 môn lại rồi chia 3
    trung_binh = (toan + ly + hoa) / 3

    # In tên và điểm trung bình, làm tròn 2 chữ số thập phân
    print(f"Sinh viên: {ten} | Điểm TB: {trung_binh:.2f}")
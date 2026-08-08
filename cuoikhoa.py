print("===== NHÀ HÀNG PYTHON =====")

tong_tien_mon = 0
hoa_don = ""
gia = 0
ten_mon = ""
thanh_tien = 0
tong_tien = 0
vat = 0

while True:
    print("1. Cơm gà - 45000 VNĐ")
    print("2. Cocacola - 15000 VNĐ")
    print("0. Thanh toán")

    mon = int(input("Chọn món: "))

    if mon == 0:
        break

    so_luong = int(input("Nhập số lượng: "))

    if mon == 1:
        ten_mon = "Cơm gà"
        gia = 45000

    elif mon == 2:
        ten_mon = "Cocacola"
        gia = 15000
    else:
        print("Món không hợp lệ!")
        continue

    thanh_tien = gia * so_luong

    tong_tien_mon = tong_tien_mon + thanh_tien

    hoa_don = hoa_don + ten_mon + " x " + str(so_luong) + \
              " = " + str(thanh_tien) + " VNĐ\n"

    print("Đã thêm", ten_mon)


vat = tong_tien_mon * 0.08

tong_tien = tong_tien_mon + vat


print("\n===== HÓA ĐƠN =====")

print(hoa_don)

print("----------------------")
print("Tiền món:", tong_tien_mon, "VNĐ")
print("VAT 8%:", vat, "VNĐ")
print("----------------------")
print("Tổng tiền:", tong_tien, "VNĐ")

print("======================")
print("Cảm ơn quý khách!")
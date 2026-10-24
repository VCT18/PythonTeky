# Database (cơ sở dữ liệu): nơi lưu trữ dữ liệu có tổ chức.
# Table (bảng): nơi lưu các dữ liệu cùng loại, ví dụ bảng sản phẩm.
# Column (cột): thuộc tính của sản phẩm, ví dụ tên, giá, số lượng.
# Row (hàng/bản ghi): thông tin của một sản phẩm cụ thể.
# SQLite: hệ quản trị cơ sở dữ liệu gọn nhẹ, lưu dữ liệu trong một tệp,
#         không cần cài đặt máy chủ riêng.

# ví dụ
# Danh sách sản phẩm của cửa hàng
# Mã SP	Tên sản phẩm	Giá	    Số lượng
# 1	    Bàn phím	    250000	10
# 2	    Chuột máy tính	150000	20
# 3	    Tai nghe	    350000	15  


import sqlite3
conn = sqlite3.connect("shop.db")  # tạo kết nối đến cơ sở dữ liệu
cursor = conn.cursor()  # tạo con trỏ để thực hiện các lệnh SQL

cursor.execute('''
CREATE TABLE IF NOT EXISTS products 
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL,
    quantity INTEGER
)
''')
conn.commit()  # lưu các thay đổi vào cơ sở dữ liệu

# cursor.execute('''
# INSERT INTO products (id, name, price, quantity) VALUES
# (1, 'Bàn phím ', 250000, 10),
# (2, 'Chuột máy tính', 150000, 20),
# (3, 'Tai nghe', 350000, 15)
# ''')
conn.commit()  # lưu các thay đổi vào cơ sở dữ liệu

cursor.execute('SELECT * FROM products')  # truy vấn tất cả các sản phẩm
rows = cursor.fetchall()  # lấy tất cả các bản ghi
for row in rows:
    print(row)

cursor.execute('SELECT * FROM products WHERE price > 200000') 
# truy vấn các sản phẩm có giá > 200000

cursor.execute('SELECT * FROM products WHERE name LIKE "%Chuột%"')
# truy vấn các sản phẩm có tên chứa từ "Chuột"

cursor.execute('UPDATE products SET quantity = 25 WHERE id = 2')
# cập nhật số lượng sản phẩm có id = 2 thành 25
conn.commit()  # lưu các thay đổi vào cơ sở dữ liệu

cursor.execute('DELETE FROM products WHERE id = 3')
# xóa sản phẩm có id = 3
conn.commit()  # lưu các thay đổi vào cơ sở dữ liệu

conn.close()  # đóng kết nối đến cơ sở dữ liệu  
# Bài 2: Khai báo biến trong python


# 1, Khai báo biến trong python.

# tenBien = giaTri

# Trong đó:
# tenBien là tên của biến mà các bạn muốn đặt. Tên biến này không được bắt đầu bằng số hay các ký tự đặc biệt, mà chỉ được bắt đầu bằng chữ cái hoặc ký tự _ và nó có phân biệt hoa thường.
# giaTri là giá trị của biến mà bạn muốn gán.

# ví dụ
name = "trần quốc trung"
print(name)

s = 4*3
print(s)
name,age,male = "trung",18,True
print(name,age,male)

# 2, Các kiểu dữ liệu trong Python.

name = "tranquoctrung" # kiểu kí tự str
age = 22 # kiểu số nguyên int
point = 8.9 # kiểu số thực float
lst = [1,2,3] # kiểu list
tup1 = (1,2,33) # kiểu tup
set1 = {12,23} # kiểu set
dic = {"key":123} # kiểu Dictionary

# 3, Kiểm tra kiểu dữ liệu.
# sử dụng hàm type 
name = "tranquoctrung" # kiểu kí tự str
print(type(name))
age = 22 # kiểu số nguyên int
print(type(age))
point = 8.9 # kiểu số thực float
print(type(point))
lst = [1,2,3] # kiểu list
print(type(lst))
tup1 = (1,2,33) # kiểu tup
print(type(tup1))
set1 = {12,23} # kiểu set
print(type(set1))
dic = {"key":123} # kiểu Dictionary
print(type(dic))


# 4, Ép kiểu dữ liệu trong Python.
# Trong một trường hợp nào đó mà bạn muốn chuyển đổi kiểu dữ liệu của một biến, thì Python cũng hỗ trợ bạn qua các hàm cơ bản sau:

# float(data) chuyển đổi sang kiểu số thực.
# int(data,base) chuyển đổi sang kiểu số, trong đó base là kiểu hệ số mà các bạn muốn chuyển đổi sang (tham số này có thể bỏ trống).
# str(data) chuyển đổi sang dạng chuỗi.
# tuple(data) chuyển đổi sang kiểu Tuple.
# dict(data) chuyển đổi sang kiểu Dictionary.
# ...

print("\n")
# ví dụ

age = 22 # đang ở kiểu số nguyên

# ép kiểu sang float
float_age = float(age)
print(type(float_age))

# ép kiểu sang chuỗi
str_age = str(age)
print(type(str_age))
# Bài 5: Số trong Python

# Ở bài trước chúng ta đã được tìm hiểu về kiểu dữ liệu chuỗi - String trong Python rồi và chuỗi trong Python được hỗ trợ rất mạnh, không biết đối với kiểu dữ liệu số - number trong Python có được hỗ trợ mạnh như chuỗi không nhé.

# 1, Kiểu dữ liệu số - number trong Python.

# Một biến được khai báo là kiểu dữ liệu number trong Python thì xét về mặt lưu trữ bộ nhớ thì nó sẽ không thay đổi được giá trị, mà khi chúng ta gán giá trị mới cho biến đó thì thực chất nó sẽ tạo ra các ô nhớ mới khác để lưu trữ giá trị mới đó.

# Trong Python hỗ trợ chúng ta 3 kiểu dữ liệu dạng number như sau:

# int kiểu số nguyên kiểu này có kích thước không giới hạn (python 2 thì bị hạn chế).
# float kiểu số thực. Kiểu này ngoài kiể viết bình thường ra thì nó cũng có thể được hiển thị dưới dạng số mũ E (VD: 2.5e2 = 250).
# complex kiểu số phức đây là kiểu dữ liệu rất ít khi được sử dụng tới, nên mình sẽ không giải thích thêm ở đây.
 
# Nếu như bạn muốn giải phóng một vùng nhớ cho một biến trong Python thì bạn có thể sử dụng lệnh del với cú pháp sau:

# del avariableName
# //hoặc xóa nhiều biến
# del avariableName1, avariableName2,..., avariableName3

# Trong đó, avariableName, avariableName1,... là các biến mà bạn muốn giải phóng.
# VD:
age = 22
print(age)
print(type(age))

del age
print(age) # age đã bị xóa nên nó báo lỗi
# 3, Các toán tử.
# Vì phần này nó giống với các ngôn ngữ khác nên mình cũng chỉ chú thích qua cho các bạn biết thôi nhé!

# Ở đây mình ví dụ biến a = 5 và b = 10:

# Toán Tử	Ví Dụ	Chú Thích
# +	a + b  // 15	Phép cộng.
# -	a - b // -5	Phép trừ.
# *	a * b // 50	Phép nhân.
# /	a / b // 0.5	Phép chia.
# %	a % b // 5	Phép chia lấy dư.
# // a // b // phép chia lấy phần nguyên
# a ** b phép lũy thừa
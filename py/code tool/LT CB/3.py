# Bài 3: Hàm print trong Python

# Trong các ngôn ngữ lập trình thì nó luôn luôn tồn tại một hoặc nhiều hàm được cùng để hiển thị dữ liệu ra khi chương trình chạy. VD như trong C thì có printf, trong C++ thì có cout,... Và đối với python thì nó là print.

# 1, Hàm print trong Python.

# Hàm print trong Python có tác dụng hiển thị dữ diệu ra màn hình khi chương trình thực thi. Sử dụng với cú pháp như sau:
# print(content)
# Trong đó: content là nội dung hay biến mà bạn muốn in ra màn hình, nếu muốn hiển thị nhiều nội dung khác nhau trên cùng một lần print thì mọi chúng ta chỉ cần ngăn các giữa các nội dung bằng dấu ,.
# VD: Hiển thị ra màn hình dòng chữ "Toidicode.com".
print("Toidicode.com")

print("Toidicode.com", " Created by thanhtaivtt")


# 2, Thay đổi ngắt dòng print.
# print sẽ có 2 thuộc tính là end và sep

# end 
print(123,end=" ")
print(567)
# thay đổi phần xuống hàng của print thành dấu cách.

# sep thay đổi kí tự giữa mỗi dấu cách khi in ra bằng dấu _
print(1,2,3,4,5,sep="_") 
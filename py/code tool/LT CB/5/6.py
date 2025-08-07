# Bài 6: List trong Python

# Ở các bài trước chúng ta đã được tìm hiểu về 2 kiểu dữ liệu string và number trong Python rồi, bài này chúng ta sẽ tiếp tục tìm hiểu về kiểu dữ liệu thứ 3 trong Python đó là list.

# 1, List là gì? và khai báo list trong Python.


# List trong Python là một dạng dữ liệu cho phép lưu trữ nhiều kiểu dữ liệu khác nhau trong nó, và chũng ta có thể truy xuất đến các phần tử bên trong nó thông qua vị trí của phần tử đó trong list. Ở đây, nếu như bạn nào đã tìm hiểu qua một ngôn ngữ nào đó thì có thể coi list trong Python như một mảng tuần tự trong các ngôn ngữ khác.

# Để khai báo một list trong Python thì chúng ta sử dụng cặp dấu [] và bên trong là các giá trị của list.

# [value1, value2,..., valueN]
# Trong đó: value1, value2,..., valueN là các giá trị của list.
# VD: Mình sẽ khai báo 1 list chứa tên các học sinh.

# name = ['VU Thanh Tai', 'Nguyen Van A', 'Nguyen Thi E']

# 2, Truy cập đến các giá trị trong list.

# Để truy cập đến các phần tử trong list thì các bạn làm tương tự như đối với chuỗi.

# Các phần tử trong một list được đánh dấu bắt đầu từ 0 theo chiều từ trái sang phải và từ -1 theo chiều từ phải qua trái.

# VD: Mình sẽ truy xuất đến từng phần tử một của list trong VD trên.

name = ['Vu Thanh Tai', 'Nguyen Van A', 'Nguyen Thi E']
print(name[0]) # Vu Thanh Tai
print(name[1]) # Nguyen Van A
print(name[2]) # Nguyen Thi E
# hoặc
print(name[-3]) # Vu Thanh Tai
print(name[-2]) # Nguyen Van A
print(name[-1]) # Nguyen Thi E

# Trong trường hợp bạn muốn in ra một phần của list thì bạn sử dụng cú pháp sau:
# list[start:end:step]

# Trong đó:

# list là tên của biến chứa list.
# start là ví trí bắt đầu lấy ra list con. Nếu để trống thì nó sẽ lấy từ đầy list.
# end là vị trí kết thúc. Nếu để trống thì nó sẽ lấy đến phần tử cuối cùng của list.
# VD:  Lấy ra 2 phần tử đầu của list trên.

name = ['Vu Thanh Tai', 'Nguyen Van A', 'Nguyen Thi E']
print(name[0:2])
# ['Vu Thanh Tai', 'Nguyen Van A']

# hoặc

print(name[-3:-1])
# ['Vu Thanh Tai', 'Nguyen Van A']

# 3, Sửa đổi và xóa bỏ giá trị phần tử trong list.

# Sau khi bạn đã truy cập được đến các phần tử trong list rồi thì bạn có thể xử lý nó như nào tùy thích theo ý của bạn (sửa - xóa).

# Update
# Để sửa giá trị của các phần tử trong list thì các bạn chỉ cần truy cập đến phần tử mà mình cần sửa đổi và tiến hành gán giá trị mới cho nó.

# VD: Sửa name thứ 2 trong list ở ví dụ trên thành 1996.


name = ['Vu Thanh Tai', 'Nguyen Van A', 'Nguyen Thi E']
print(name)
# ['Vu Thanh Tai', 'Nguyen Van A', 'Nguyen Thi E']

name[1] = 1996
print(name)
# ['Vu Thanh Tai', 1996, 'Nguyen Thi E']

# Để xóa một hoặc nhiều phần tử trong list thì các bạn cần truy cập đến phần tử cần xóa và dùng hàm del để xóa. Và sau khi chúng ta xóa phần tử trong list thì index của list sẽ được cập nhật lại.

# VD: Xóa phần tử thứ 3 trong list trên.


name = ['Vu Thanh Tai', 'Nguyen Van A', 'Nguyen Thi E']
print(name)
# ['Vu Thanh Tai', 'Nguyen Van A', 'Nguyen Thi E']

del name[2]
print(name)
# ['Vu Thanh Tai', 'Nguyen Van A']

# 4, List lồng nhau.

# Do list có thể chứa nhiều kiểu dữ liệu khác nhau lên chúng ta hoàn toàn có thể khai báo một list chứa một hoặc nhiều list khác nhau.

option = [12,5,1996]
myList = ['Vu Thanh Tai', option]
print(myList)
# ['Vu Thanh Tai', [12, 5, 1996]]

# Và cứ như thế chúng ta có thể lồng N list khác vào trong list.

# Đối với list lồng nhau như này thì chúng ta chũng truy xuất đến các phần tử như bình thường, theo cấp từ ngoài vào trong.

# VD: Mình sẽ truy cập vào phần tử dầu tiên trong list option.

option = [12,5,1996]
myList = ['Vu Thanh Tai', option]
print(myList)
# ['Vu Thanh Tai', [12, 5, 1996]]

subList = myList[1] # [12, 5, 1996]
subList[0] # 12

# hoặc có thể viết ngắn gọn như sau
myList[1][0] # 12
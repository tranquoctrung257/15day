# Bài 4: Chuỗi trong Python

# Tất cả các ngôn ngữ lập trình đều có kiểu dữ liệu là kiểu chuỗi, và trong Python nó cũng không ngoại lệ. Bài này mình sẽ cùng mọi người tìm hiểu xem chuỗi trong Python có ưu điểm gì hơn các ngôn ngữ khác không nhé.

# 1, Các ký tự đặc biệt trong chuỗi.
# VD: Khi bạn muốn in ra "  mà bạn lại sử dụng  "" để chứa nội dung int ra chuỗi.

print("Website \"Toidicode.com\" ")
#Website "Toidicode.com"

print('Website \'Toidicode.com\' ')
#Website 'Toidicode.com'

# Các ký tự đặc biệt khác:

# \n ngắt xuống dòng và bắt đầu dòng mời.
# \t đẩy nội dung phía sau nó cách 1 tab.
# \a chuông cảnh báo.
print("\a")
# \b xóa bỏ khoảng trắng phía trước nó.
print("trung \b")
# Ngoài ra bạn cũng có thể sử dụng để in ra các ký tự đặc biệt khác bằng việc sử dụng theo cú pháp \xnn, với n là 0->9, hoặc a->f hoặc A->F.

# 2, Fomat chuỗi.
# Ngoài những cách in ra dữ liệu ở trên thì mọi người cũng có thể sử dụng các keyword định dạng cho kiểu giá trị và binding nó vào chuỗi. Sử dụng với cú pháp:

# print("%type" %(binding))

# Trong đó:

# type là các kiểu dữ liệu các bạn muốn binding và thay thế vào vị trí đó.
# binding là giá trị mà các bạn muốn binding vào vị trí được xác định trong chuỗi.
# Type là các kiểu sau:

# Cú pháp fomat	Mô tả
# %c	character
# %s	chuỗi
# %i	số nguyên
# %d	số nguyên
# %u	số nguyên
# %o	bát phân
# %x	thập lục phân (in thường)
# %X	thập lục phân (in hoa)
# %e	số mũ  (với e thường)
# %E	số mũ  (với e hoa)
# %f	số thực
# %g	dạng rút gọn của %f and %e
# %G	dạng rút gọn của %f and %E

# VD: Mình sẽ thực hiện binding 1 chuỗi vào trong 1 chuỗi.

guy = "Ban"
full = "Chao mung %s den voi website toidicode.com" %(guy)
print(full)
# Chao mung Ban den voi website toidicode.com

print("xin chào tôi là %s"%("trung"))
# 3, Truy cập tới từng giá trị của chuỗi.

# chuỗi sử dụng giống list 

# Chuỗi trong Python được lưu trữ vào trong các ô nhớ với mỗi ô nhớ tương đương với một ký tự đơn (khác với các ngôn ngữ khác) và các ký tự này được xếp liên tiếp với nhau. Do đó kiểu dữ liệu chuỗi trong Python có thể được truy xuất đến từng ký tự trong nó (các ngôn ngữ khác không có, PHP7.1.X mới hỗ trợ ở đây là reverse index string).

# Để truy cập đến từng ký tự bên trong chuỗi, các bạn sử dụng cú pháp sau:

# stringName[index]
# Trong đó:

# stringName là tên của biến chứa chuỗi, hoặc chuỗi.
# index là vị trí của ký tự bạn muốn lấy ra. Index này hỗ trợ chúng ta truy xuất được cả 2 chiều của chuỗi nếu:
# Tính từ đầu thì nó bắt đầu từ 0.
# Tính từ cuối thì nó bắt đầu từ -1.

# VD
name = "Vu Thanh Tai"
print(name[0]) # V
print(name[-1]) # i

# Nếu trong trường hợp các bạn muốn lấy nội dung của một đoạn chuỗi trong chuỗi đó thì có thể sử dụng cú pháp sau:

# stringName[start:end]

# Trong đó:

# stringName là tên của biến chứa chuỗi, hoặc chuỗi.
# start là vị trí của ký tự bắt đầu lấy, nếu để trống start thì nó sẽ lấy từ 0.
# end là vị trí kết thúc (nó sẽ lấy trong khoảng từ start đến < end), nếu để trống end thì nó sẽ lấy đến hết chuỗi.

# VD
name = "Vu Thanh Tai"

print(name[0:2]) # Vu

print(name[-3:12]) # Tai

print(name[9:]) # Tai

print(name[-3:]) # Tai

print(name[:])

print(name[1:-1:2])
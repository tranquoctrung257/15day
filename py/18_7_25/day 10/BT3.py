# 3. Cho dict như sau:
people = {
  "Emma": 71,
  "Jack": 45,
  "Amy": 15,
  "Ben": 29
}
m = 0
# + In ra người già nhất
for i in people.values():
    if i > m:
        m = i
print(m)


# + Tạo ra một dict mới dựa vào people dict với tuổi của mỗi người tăng gấp đôi
dic = {
    k:v*2 for k,v in people.items()
}
print(dic)
# + In ra enumerate các key trong people dict
print(list(enumerate(people)))
# + Sử dụng hàm dict để biến enumerate bên trên trở thành dict
lst = dict(enumerate(people))
print(lst)
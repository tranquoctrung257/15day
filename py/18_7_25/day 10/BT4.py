# 4. Sử dụng zip function để tạo 2 lists sau trở thành một dict
fruits  = ["banana", "apple", "kiwi", "mango", "cherry", "orange"]
amounts = [12, 34, 90, 100, 300, 45, 60, 70, 678]

print(dict(zip(fruits,amounts)))
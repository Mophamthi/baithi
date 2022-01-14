name = str(input("Nhập tên: "))
print(len(name))
n = int(input("Nhập số n = "))
a = dict()
for i in range(1, n + 1):
    a[i] = i * i
print(a)
name = str(input("Nhập tên mình và tên đệm: "))
print(len(name)
def totalDigitsOfNumber(n):
    total = 0;
    while (n > 0):
        total = total + n % 10;
        n = int(n / 10);
    return total;
n = int(input("Nhập số n = "));
print("Tổng các chữ số của", n, "là", totalDigitsOfNumber(n));
# Найдите сумму цифр трехзначного числа.
# in
# 123

num = int(input("Введите трехзначное число "))
res = 0
while num > 0:
    res += num % 10
    num //= 10

print(res)

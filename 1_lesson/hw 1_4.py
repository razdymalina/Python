# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# in
# 3 2 4
# out
# yes

n = int(input())
m = int(input())
k = int(input())

if (k % n == 0 or k % m == 0) and k < m * n:
    print("Да")
else:
    print("Нет")

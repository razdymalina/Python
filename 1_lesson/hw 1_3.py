# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# in123321
# 385916
# out
# yes

num = input("Введите номер билета: ")
sum_one = int(num[0]) + int(num[1]) + int(num[2])
sum_two = int(num[3]) + int(num[4]) + int(num[5])

print(f"Счастливый билет: {sum_one == sum_two}")


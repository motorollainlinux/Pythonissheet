from math import sqrt

# задача №1
x = int(input("Enter X:"))
y = int(input("Enter Y:"))
if x < 0:
    if x > y:
        z = x
    else: 
        z = y
else:
    z = (x + y)/2
print("Z: ", z)

# # задача №2
# a = int(input("Enter a:"))
# b = int(input("Enter b:"))
# c = int(input("Enter c:"))
# D = b**2-4*a*c
# if D > 0:
#     xf = round((-b+sqrt(D))/(2*a), 3)
#     xs = round((-b-sqrt(D))/(2*a), 3)
#     print("x1: ", xf, " x2: ", xs)
# elif D == 0:
#     x = round((-b)/(2*a), 3)
#     print("x: ", x)
# else:
#     print("Roots is not exist.")

# # задача №3
# x = int(input("введите число: "))
# if x % 2 == 0:
#     print("Оно чётное; ")
# if x % 10 == 7:
#     print("Оно оканчивается на 7; ")
# if x % 13 == 0:
#     print("Оно делится на 13;\n")
    
# # задача №4
# x = int(input("введите число: "))
# a = x //100
# b = (x // 10)% 10
# c = x % 10
# if a == b and b == c:
#     print("все цифры числа равны.")
# elif a == b:
#     print("первая и вторая цифры числа равны")
# elif b == c:
#     print("вторая и третья цифры числа равны")
# elif a == c:
#     print("первая и третья цифры числа равны")
# else:
#     print("все цифры числа разные")

# # задача №5
# x = int(input("введите четырёхзначное число: "))
# t = int(input("введите число t: "))
# if x//1000 + ((x//100)%10) == ((x//10)%10) + x%10:
#     print("сумма двух первых цифр числа равна сумме двух его последних цифр;")
# if (x//1000 + ((x//100)%10) + ((x//10)%10) + x%10)% 3 == 0:
#     print("сумма его цифр кратна 3;")
# if (x//1000 + ((x//100)%10) + ((x//10)%10) + x%10)%t == 0:
#     print("сумма его цифр кратна t;")
# if x//1000 == x%10 and ((x//100)%10) == ((x//10)%10):
#     print("число является палиндромом;")

# # задача №6
# x = int(input("Прямо(введите 0), направо (введиете 1), налево (введите -1)"))
# if x == 0:
#     print("в ВУЗ на программиста поступишь")
# elif x == 1:
#     print("поваром станешь")
# elif x == -1:
#     print("учителем физкультуры станешь")
# else: 
#     print("неверно введите 0 или 1 или -1")

# # задача №7
# # I
# a = int(input("1: "))
# b = int(input("2: "))
# c = int(input("3: "))
# if a >= b and a >= c:
#     print("максимум: ", a)
# elif b >= a and b >= c:
#     print("максимум: ", b)
# else:
#     print("максимум: ", c)

# # II
# a = int(input("1: "))
# b = int(input("2: "))
# c = int(input("3: "))
# if a > b:
#     if a > c:
#         print("максимум: ", a)
#     else:
        # print("максимум: ", c)
# else:
#     if b > c:
#         print("максимум: ", b)

# # III
# a = int(input("1: "))
# b = int(input("2: "))
# c = int(input("3: "))
# if a > b:
#     M = a
# else:
#     M = b
# if M > c:
#     print("максимум: ", M)
# else:
#     print("максимум: ", c)
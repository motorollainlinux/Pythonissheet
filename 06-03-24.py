# задача №1
result = 1
for i in range(1, 10, 2):
    result *= i
for i in range(0, 10, 2):
    result += i
print(result)

# # задача №2
# result = 1
# a = int(input("input a: "))
# n = int(input("input n: "))
# for i in range(n):
#     result *= a
# print("result: " , result)

# # задача №3
# left = int(input("input left: "))
# right = int(input("input right: "))
# for i in range(left, right, 1):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i)

# #задача №4
#I
# result = 1
# for i in range(2, 14, 3):
#     result *= i
# print(result)
#II
# result = 1
# i = 2
# while(i < 14):
#     result *= i
#     i += 3
# print(result)

# #задача №5
# while True:
#     left = int(input("input left: "))
#     right = int(input("input right: "))
#     if(left < 0 and right < 0 and left < right):
#         for i in range(left, right, 1):
#             if i % 3 == 0 and i % 5 == 0:
#                 print(i)
#         break
#     else:
#         print("Input is Invalid!")
    
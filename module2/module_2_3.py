my_list = [-5, 9, 8, 7, -6, 5]
index = 0
while index < len(my_list) and my_list[index] >= 0:
    if my_list[index] != 0:
        print(my_list[index])
    index += 1

#Или такой вариант с импользованием break, continue
# while index < len(my_list):
#     if my_list[index] < 0:
#         break
#     if my_list[index] == 0:
#         index +=1
#         continue
#     print(my_list[index])
#     index += 1

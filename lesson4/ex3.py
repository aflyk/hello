my_list_1 = [2, 2, 5, 12, 8, 2, 12]
for i in my_list_1:
    if my_list_1.count(i) > 1:
        for j in range(my_list_1.count(i)):
            my_list_1.remove(i)
print(my_list_1)
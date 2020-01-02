my_list1 = [1,2,1,12,20,13]
my_list2 = [1, 7, 12, 576]
for i in my_list2:
    if i in my_list1:
        for j in range(my_list1.count(i)):
            my_list1.remove(i)

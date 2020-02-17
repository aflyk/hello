def some_f(k):
    k = [1 for i in k]
    return k

def some_f1(k):
    k[:] = [1 for i in k]
    return k


lst = [1, 2, 3]
print(some_f(lst))
# после выполнения функции выполняем проверку листа
print(lst)
# выполяем вторую функцию
print(some_f1(lst))
# проверяем значение переменной lst
print(lst)

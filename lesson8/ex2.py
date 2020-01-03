def eq_f(a,b,c):
    if a >= b and a >= c: return a
    elif b >= c and b >= a: return b
    else: return c

a = float(input())
b = float(input())
c = float(input())
print(eq_f(a, b, c))

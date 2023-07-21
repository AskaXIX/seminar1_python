# # Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, 
# то есть выведите такое число n, что φ(n)=A. 
# # Если А не является числом Фибоначчи, выведите число -1.

n = int(input("n: "))

fibo_prev = 0
fibo_cur = 1
index = 1

while fibo_cur < n:
    fibo_prev, fibo_cur = fibo_cur, fibo_prev + fibo_cur
    index += 1
if fibo_cur == n:
    print(f"Число {n} идет {index} числом в последовательности Фибоначчи")
else:
    print(-1)
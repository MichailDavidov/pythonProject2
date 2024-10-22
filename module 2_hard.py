import math

def parols_num (num):
    parols = []
    num1 = int(math.ceil(num/2))
    a = 2
    for i in range (1, num1):
        for j in range (a, num):
            summa = i + j
            if num % summa == 0:
                parols.append (i)
                parols.append (j)
        a +=1
    return parols
numeric = int(input("Введите число "))
parol = parols_num (numeric)
print (numeric,":",parol)
# Даны два неупорядоченых набора целых чисел( может быть с повторениями).
# выдать без повторений в порядке возрастания все те числа , которые встречаются
# в обоих  наборах.
# Пользователь вводит 2 числа.n - колличество элементов первого множества.
# m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.
n = int(input("Введите длину первого множества :"))
many1 = []
for _ in range(n):
    num=int(input())
    many1.append(num)
print(many1)
many3 = set(many1) 

m = int(input("Введите длину второго множества:"))  
many2 = []
for _ in range(m):
    numm=int(input())
    many2.append(numm)
print(many2)
many4 = set(many2)

many12 = many3.union(many4)
print(sorted(many12))
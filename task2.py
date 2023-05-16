# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import functions

list2 = [1, 3, 4, -5, -6, 6]
maxx = int(functions.number_creat())
minn = int(functions.number_creat())

print(functions.min_max(maxx,minn,list2))
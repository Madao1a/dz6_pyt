def number_creat():
    n = input("Введите число ")
    return n

def list_create(n,m,l):
    sum = n
    list1 = []
    for i in range(1,l+1):
        list1.append(sum)
        sum += m
    return list1

def min_max(m, n, list_2):
    list3 = []
    for i in range(len(list_2)):
        if n <= list_2[i] <= m:
            list3.append(i)
    return list3



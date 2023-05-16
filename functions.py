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

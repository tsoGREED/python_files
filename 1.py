'''
База данных
товары (категория, название товара, id, price, description)
заказы (id_order, date_order)
ибранные (товар)

r(read) - чтение
w(write) - перезапись
a(append) - дозапись
'''

#f = open('numbers1.txt', 'r') #FileNotFoundError
#print(f.read())
#print(f.read(10)) #1 символ - 1 байт
#print(f.readline())
#print(f.readlines())
#f.close()


#f = open('numbers.txt', 'a')
#f.write('\n1 2\t 31 86')
#f.close()


#контексный менеджер
with open('numbers.txt', 'a', encoding='utf-8') as f:
    f.write('\nпривет мир')


with open("nums.txt", "r") as f:
    nums = f.readlines()
    print(nums)
    a = []
    for i in nums: #i='1\n' i='3\n' ... i='76'
        print(int(i))
        a.append(int(i))
    print(sum(a))
'''
int 76
float 76.5
str '76'
bool

list (список) [] изменяемый
tuple (кортеж) () неизменяемый
dict (словарь) {} изменяемый
set (множества) {} изменяемый
'''


n = [4, 5, 6, 1, 2]
#    0  1  2  3   4
#ф-ции
print(len(n))
n[0] = 10
print(n)
print(sum(n))
print(min(n))
print(max(n))
print(sorted(n))
print(sorted(n, reverse=True))

#методы
a = []
a.append(1)
a.append(2)
a.append(3)
print(a)
a.insert(0, 0)
print(a)
a.extend([4, 5, 6])
print(a)

a.remove(0)
print(a)
a.append(6)
print(a)
a.remove(6)
print(a)
a.pop(0)
print(a)
#sorted()
#a.sort()


#tuple
c = (1, 2, 3, 4)
#c[0] = 1
print(c[0])
d = 1, 2, 3, 4, 5
print(type(d))

d1 = (1,)
print(type(d1))
print(len(d1))
print(sum(d1))
print(min(d1))
print(max(d1))


#dict
a = [1, 2, 3]
#    0  1  2
f = {'a': 1, 'b': 2, 'c': 3}
#         'a'     'b'     'c'
print(a[0])
print(f['a'])


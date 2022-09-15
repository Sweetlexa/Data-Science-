# Задание 1
with open('file1.txt', 'a', encoding='utf-8') as f:
    while True:
        data = input('Введите текст:')
        n = '\n'
        if data != '':
            f.write(f'{data}{n}')
        else:
            break

# Задание 2
with open('file2.txt', 'r', encoding='utf-8') as f:
    n = f.readlines()
    print(n)
    m = len(n)
    print('Количество строк: ',m)
    i = 1
    for el in n:
        if ' ' in el:
            c = el.count(' ')
            c = c + 1
            print('Количество слов в', i ,'строке:', c)
            i = i + 1
        else:
            print('Количество слов в', i, 'строке: 1')
            i += 1

# Задание 3
with open('file3.txt', 'r', encoding='utf-8') as f:
    li = f.readlines()
    print(li)
    i = 0
    for el in li:
        n = el.index(' ')
        v = (el[n+1:len(el)-1])
        v = float(v)
        k = (el[:n])
        if v > 20000.0:
            print('Зарплата данного сотрудника больше 20 тысяч: ', k)
            i = i + v
    z = i / len(li)
    print('Средняя величина дохода сотрудников: ', z)

# Задание 4
f = open('file4.txt', 'r', encoding='utf-8')
li = f.readlines()
print(li)
i=0
while i < len(li):
    li.pop(i)
print(li)
li.append('один - 1\n')
li.append('два - 2\n')
li.append('три - 3\n')
li.append('четыре - 4\n')
print(li)
f1 = open('file4_1.txt', 'a', encoding='utf-8')
f1.writelines(li)

f1.close()
f.close()

# Задание 5
with open('file5.txt', 'a', encoding='utf-8') as f:
    data = input('Введите числа через пробел: ').split()
    data = list(map(int,data))
    s = sum(data)
    print('Cумма чисел: ', s)




import random


# a = int(input('Kiek darbuotojas gali iskepti kepalu per valanda? '))
# b = int(input('Kiek darbuotoju turi kepykla? '))
# c = int(input(f'Vieno kepalo savikaina? '))
# d = int(input('Vieno kepalo pardavimo kaina? '))
# e = int(input('Kiek kepykla turi ta diena iskepti kepalu (uzsakymai)? '))
#
# dv = 8
#
# print(f'Kepykla per viena diena suspes iskepti {dv * a}')
# g = dv * a
# savikaina = g * c
# pelnas= d * g
# print(f'Pilna pelno dalys {pelnas - savikaina} Eur')
#
# if e < g:
#     print('suspes iskepti')
# elif e > g:
#     print(f'Nesuspes iskepti {e - g} kepalu')

# kiek is tikruju pardavei
# 1

# name = input('Jusu vardas: ')
# surname = input('Jusu pavarde: ')
# bornyear = int(input('Jusu gimimo metai: '))
# yearnow = int(input('Kokie metai dabar: '))
#
# print(f'As esu {name} {surname}. Man yra {yearnow-bornyear} metu')

# 2

# b = random.randint(0, 4)
# a = random.randint(0, 4)
#
# if b > a:
#     c = a / b
#     ats = "{:.2f}".format(c)
#     print(ats)
# elif a > b:
#     c = b / a
#     ats = "{:.2f}".format(c)
#     print(ats)

# 3

# b = random.randint(0, 25)
# a = random.randint(0, 25)
# c = random.randint(0, 25)
#
# if b > a and b < c or b > c and a > b:
#     print(f'{b}')
# elif c > a and b > c or c > b and c < a:
#     print(f'{c}')
# elif b < a and a < c or a > c and a < b:
#     print(f'{a}')
# else:
#     print(False)

# 4

# b = random.randint(0, 10)
# a = random.randint(0, 10)
# c = random.randint(0, 10)
#
# if a + b > c and a + c > b and c + b > a:
#     print('Gali buti trikampis')
# else:
#     print('Negali')

# 5

b = random.randint(0, 2)
a = random.randint(0, 2)
c = random.randint(0, 2)
e = random.randint(0, 2)

nuliai = 0
vienetai = 0
dvejetai = 0
print(a,b,c,e)

if e == 0:
    nuliai += 1
if b == 0:
    nuliai += 1
if c == 0:
    nuliai += 1
if a == 0:
    nuliai += 1
print(f'Nuliu tiek {nuliai}')
if a == 1:
    vienetai += 1
if b == 1:
    vienetai += 1
if c == 1:
    vienetai += 1
if e == 1:
    vienetai += 1
print(f'Vienetu tiek {vienetai}')
if a == 2:
    dvejetai += 1
if b == 2:
    dvejetai += 1
if c == 2:
    dvejetai += 1
if e == 2:
    dvejetai += 1
print(f'Dvjejetu tiek {dvejetai}')
#

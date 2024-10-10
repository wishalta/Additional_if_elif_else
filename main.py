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

b = random.randint(0, 4)
a = random.randint(0, 4)

if b > a:
    c = a / b
    ats = "{:.2f}".format(c)
    print(ats)
elif a > b:
    c = b / a
    ats = "{:.2f}".format(c)
    print(ats)

# neradau :')
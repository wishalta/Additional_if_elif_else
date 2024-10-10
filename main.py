a = int(input('Kiek darbuotojas gali iskepti kepalu per valanda? '))
b = int(input('Kiek darbuotoju turi kepykla? '))
c = int(input(f'Vieno kepalo savikaina? '))
d = int(input('Vieno kepalo pardavimo kaina? '))
e = int(input('Kiek kepykla turi ta diena iskepti kepalu (uzsakymai)? '))

dv = 8

print(f'Kepykla per viena diena suspes iskepti {dv * a}')
g = dv * a
savikaina = g * c
pelnas= d * g
print(f'Pilna pelno dalys {pelnas - savikaina} Eur')

if e < g:
    print('suspes iskepti')
elif e > g:
    print(f'Nesuspes iskepti {e - g} kepalu')


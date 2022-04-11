pokedex151 = [
    {
        'Name': 'BULBASAUR',
        'Dex Num': '001',
        'Type1': 'GRASS',
        'Type2': 'POISON',
    },
    {
        'Name': 'IVYSAUR',
        'Dex Num': '002',
        'Type1': 'GRASS',
        'Type2': 'POISON',
    },
    {
        'Name': 'VENUSAUR',
        'Dex Num': '003',
        'Type1': 'GRASS',
        'Type2': 'POISON',
    },
    {
        'Name': 'CHARMANDER',
        'Dex Num': '004',
        'Type1': 'FIRE',
    },
    {
        'Name': 'CHARMELEON',
        'Dex Num': '005',
        'Type1': 'FIRE',
    },
    {
        'Name': 'CHARIZARD',
        'Dex Num': '006',
        'Type1': 'FIRE',
        'Type2': 'FLYING',
    },
    {
        'Name': 'SQUIRTLE',
        'Dex Num': '007',
        'Type1': 'WATER',
    },
    {
        'Name': 'WARTORTLE',
        'Dex Num': '008',
        'Type1': 'WATER',
    },
    {
        'Name': 'BLASTOISE',
        'Dex Num': '009',
        'Type1': 'WATER',
    },
]

def menu():
    print('{0:_^25}'.format(' POKÉDEX '))
    print('Search By Name', '{0: >10}'.format('(1)'))
    print('Search By Type', '{0: >10}'.format('(2)'))
    print('Search By Number', '{0: >8}'.format('(3)'))
    print('List By Name', '{0: >12}'.format('(4)'))
    print('List By Number', '{0: >10}'.format('(5)'))
    print('Add/Edit Pokémon', '{0: >8}'.format('(6)'))
    print('{0:_^25}'.format('_'))

def search_namenum(n):
    f = False

    for k in pokedex151:
        if n == '':
            break
        if n.upper() in k.values():
            f = True
            for i, j in k.items():
                print(f'\t{i} - {j}')

    if not f: print('NOT FOUND')


def search_type(t1, t2):
    c = 0
    for k in pokedex151:

        if t2 == '':
            if t1.upper() in k.values():
                c += 1
                print('\t', k['Name'])
        else:
            if t1.upper() in k.values() and t2.upper() in k.values():
                c += 1
                print('\t', k['Name'])
    print(f'{c} Pokemón FOUND!')


def list_dex(id):
    sorted_pokedex = sorted(pokedex151, key=lambda k: k[id])
    for k in sorted_pokedex:
        print(k['Dex Num'])
        for k1, v1 in k.items():
            print(f'\t{k1} - {v1}')


def add_ed_pok():
    nam = input('Name? ')
    num = input('Dex Num? ')
    t1 = input('Type1? ')
    t2 = input('Type2? ')
    if t2 == '':
        pokedex151.append({'Name': nam.upper(), 'Dex Num': num, 'Type1': t1.upper()})
    else:
        pokedex151.append({'Name': nam.upper(), 'Dex Num': num, 'Type1': t1.upper(), 'Type2': t2.upper()})


exit = True
while exit:
    menu()
    op = input('Input: ')
    if op == '1':
        n = input('What pokémon? ')
        search_namenum(n)
    elif op == '2':
        t = input('What type1? ')
        t1 = input('What type2? ')
        search_type(t, t1)
    elif op == '3':
        t = input('Number(XXX)? ')
        search_namenum(t)
    elif op == '4':
        list_dex('Name')
    elif op == '5':
        list_dex('Dex Num')
    elif op == '6':
        add_ed_pok()
    else:
        print('Msg Error: Invalid option!')
    s = input('Exit? y[es] n[any key] ')
    if s.lower() == 'y': exit = False


print('\n *** App Finished ***')

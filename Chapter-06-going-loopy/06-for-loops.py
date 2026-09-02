for x in range(0,5):
    print('hello')

print(list(range(10,20)))

for x in range(0,5):
    print(f'hello {x}')

wizard_list=['spider legs' , 'toe of frog' , 'snail tongue' , 'bat wing' , 'slug butter' , 'bear burp']
for ingredient in wizard_list:
    print(ingredient)

hugehairypants=['huge' , 'hairy' , 'pants']
for i in hugehairypants:
    print(i)
    print(i)

hugehairypants=['huge' , 'hairy' , 'pants']
for i in hugehairypants:
    print(i)
    for j in hugehairypants:
        print(j)

found_coins=20
magic_coins=70
stolen_coins=3
coins=found_coins
for week in range(1,53):
    coins=coins + magic_coins - stolen_coins
    print(f'Week {week}={coins}')
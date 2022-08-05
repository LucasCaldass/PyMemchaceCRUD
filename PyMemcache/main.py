import pandas as pd
from pymemcache.client import base

client = base.Client(('localhost', 11211))

def include(key, value):
    client.set(key, value)

df = pd.read_csv('sales_ts.csv')
df = df[['Sales_quantity', 'Period']]

for ind in df.index:
    include(df['Period'][ind], df['Sales_quantity'][ind])

def menu():
    print('[1] Create a instance')
    print('[2] Read a instance')
    print('[3] Update a instance')
    print('[4] Delete a instance')
    print('[0] Exit')

menu()
option = int(input('What you want to do?: '))
print()

while option != 0:
    if option == 1:
        key = input('Enter the key: ')
        value = input('Enter the value: ')
        client.set(key, value)
        print('Instance has been created.', 'key: ', key, 'value: ', value)
    elif option == 2:
        print()
        key = input('Enter the key for the value: ')
        print(client.get(key))
    elif option == 3:
        print()
        key = input('Enter the key: ')
        new_value = input('Enter the new value: ')
        client.set(key, new_value)
        print('Instance has been updated.')
    elif option == 4:
        print()
        key = input('Type the key of the value you want to delete: ')
        client.delete(key)
        print('Instance has been deleted.')
    else:
        print()
        print('Invalid option.')

    print()
    menu()
    option = int(input('What you want to do?: '))

print('End.')

client.flush_all()
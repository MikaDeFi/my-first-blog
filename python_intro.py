print('Hello, Django girls!')


if 3 > 2:
    print('It works!')
if 5 > 2:
    print('5 is indeed greater than 2')
else:
    print('5 in not greater than 2')
name = 'Mika'
if name == 'Hola':
  print('Hey Hola!')
elif name == 'Mika':
    print('Hey Mika!')
else:
    print('Hey anonymous!')

def hi():
    print('Hi there!')
    print('How are you?')
hi()

def hi(name):
    if name == 'Hola':
        print ('Hi Hola!')
    elif name == 'Mika':
        print ('Hi Mika!')
    else:
        print ('Hi anonymous!')
hi('Maria')

def hi(name):
    print ('Hi' + name + '!')

hi ("Rachel")

def hi(name):
    print ('Hi' + name + '!')
girls = ['Rachel','Monica', 'Phoebe','Hola', 'Mika']
for name in girls:
    hi(name)
    print ('Next girl')
for i in range(1, 6):
    print(i)    

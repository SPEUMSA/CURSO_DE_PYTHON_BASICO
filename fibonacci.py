contador=int(input('Ingresa un numero: '))
#Con bucle for
print('Usando For')
a=0
b=1
for i in range(0,contador):
    c=a+b
    print(a)
    a=b
    b=c
#Con un bucle while
print('Usando While')
a=0
b=1
while contador>0:
    c=a+b
    print(a)
    a=b
    b=c
    contador -= 1
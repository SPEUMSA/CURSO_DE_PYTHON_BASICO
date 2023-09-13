numeros=[1,1,3,5,78,43,22,56]
impares=0
pares=0

for i in numeros:
    if i%2==0:
        pares+=1
    else:
        impares+=1
print('Pares:',pares)
print('Impares:',impares)
#CRIAR UMA MATRIZ NA TELA 3X3

m = []
l = []

for c in range (0,3):
    for d in range (0,3):
        l.append(int(input(f'Digite um numero para [{c}, {d}]: ')))

    m.append(l[:])
    l.clear()

print(f'{m[0][0]} {m[0][1]} {m[0][2]}\n{m[1][0]} {m[1][1]} {m[1][2]}\n{m[2][0]} {m[2][1]} {m[2][2]}')

#MANIPULAR NUMEROS DA MATRIZ

s = 0
s3 = 0
maior = 0
for c in m:
    
        
for c in m:
    if c[1] == 0:
        maior = c[1]
    elif c[1] > maior:
        maior = c[1]
    for d in m:
        s = d[0] + s
        s3 = d[2] +s3

for c in m:
     for d in m:   
        if d[1] == 0:
            maior = d[1]
        elif d[1] > maior:
            maior = d[1]
    

print(s, s3, maior)

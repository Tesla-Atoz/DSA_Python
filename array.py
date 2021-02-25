exp = [2200, 2350, 2600, 2130, 2190]

print(exp[1]-exp[0])
print(exp[1]+exp[2]+exp[0])

x = 2000 in exp
print(x)


exp.insert(5, 1980)
exp[3] = exp[3]-200
print(exp)

# -----
heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

print(len(heros))
heros.append('black panther')
heros.remove('black panther')
heros.insert(heros.index('hulk')+1, 'black panther')
heros[1:3] = ['doctor strange']
heros.sort()
print(heros)

# -----
max_number = int(input('enter number'))
y = [i for i in range(max_number) if i % 2 != 0]
print(y)

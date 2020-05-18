stara = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nowa = [0, 0, 0, 0, 0]

a = 0
for i in range(5):
    nowa[i] = stara.pop()
nowa = nowa[::-1]
print(stara)
print(nowa)

lista = stara + nowa
lista = lista[::-1]
lista.append(0)
lista = lista[::-1]
kopia = lista
print(kopia[::-1])

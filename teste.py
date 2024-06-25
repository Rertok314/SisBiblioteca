lista = [{'nome' : 'elias', 'ano' : 2020}, {'nome' : 'gabriel', 'ano' : 1990}, {'nome' : 'mateus', 'ano' : 852}, {'nome' : 'arthur', 'ano' : 2005}]

n = len(lista)

n = len(lista)
for i in range(n):

    menor_indice = i
    for j in range(i+1, n):
        if lista[j]['nome'] < lista[menor_indice]['nome']:
            menor_indice = j

    lista[i], lista[menor_indice] = lista[menor_indice], lista[i]

print("Sorted array:", lista)
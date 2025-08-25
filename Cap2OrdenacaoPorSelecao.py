# A ordenação por seleção é um algoritmo bom, mas não é muito rápido
# O quicksort é um algoritmo de ordenação mais rápido, que tem tempo de
# execução de apenas O(n log n). Será melhor abordado no Capítulo 4.

#Exemplo:

def busca_menor(arr):
    menor = arr[0]
    menor_indice = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice

def ordenacao_por_selecao(arr):
    novoarr = []
    for i in range(len(arr)):
        menor = busca_menor(arr)
        novoarr.append(arr.pop(menor))
    return novoarr


print(ordenacao_por_selecao([5, 3, 6, 2, 10]))
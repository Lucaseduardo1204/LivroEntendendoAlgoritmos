# O algoritmo Quicksort é um algoritmo de ordenação muito mais rápido
# do que o algoritmo de ordenação por seleção.
#
# Ele utiliza a técnica de Dividir para Conquistar (DC), que consiste em:
# 1. Dividir o problema em subproblemas menores.
# 2. Resolver recursivamente cada subproblema.
# 3. Combinar os resultados.
#
# Esse processo continua até chegar ao "caso base",
# que é o menor problema possível, resolvido diretamente.

# [2, 5, 1, 3, 10, 60]

def quicksort(array):
    if len(array) < 2:
        return array #1º
    else:
        pivo = array[0] #2º
        menores = [i for i in array[1:] if i <= pivo] #3º
        maiores = [i for i in array[1:] if i > pivo] #4º
        return quicksort(menores) + [pivo] + quicksort(maiores)

    # 1 - Caso-base: Arrays com 0 ou 1 elemento já estão ordenados.
    # 2 - Escolha do pivô: Aqui pegamos o primeiro elemento como pivô.
    # 3 - Subarray com todos os elementos **menores ou iguais** ao pivô.
    #     (list comprehension: para cada elemento em array[1:], se for <= pivô, vai para 'menores').
    # 4 - Subarray com todos os elementos **maiores** que o pivô.
    #     (list comprehension: para cada elemento em array[1:], se for > pivô, vai para 'maiores').




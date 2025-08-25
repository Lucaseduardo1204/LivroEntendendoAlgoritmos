# Pesquisa Binária
# ----------------
# Imagine que você queira adivinhar um número entre 1 e 100.
# Em vez de testar cada número um por um (como faria na pesquisa linear),
# você sempre chuta o número do meio.
#
# - Se o número que você procura for menor que o chute,
#   você descarta toda a metade maior.
# - Se for maior, descarta a metade menor.
# - Se acertar, encontrou a resposta!
#
# Assim, a cada passo você corta o conjunto de números restantes pela metade,
# tornando a busca muito mais rápida do que verificar todos de forma sequencial.
# Esse é o princípio da pesquisa binária.

# Exemplo:

def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None

minha_lista = [1, 3, 5, 7, 9]

print(pesquisa_binaria(minha_lista, 3))
print(pesquisa_binaria(minha_lista, -1))


# Na pesquisa simples 100, números seriam necessárias 100 tentativas no pior dos casos
# 4 Bilhões de números, seriam necessárias 4 bilhões de tentativas
# Já na pesquisa binária, se uma lista tem 100 itens, precisaria de, no máximo, 7 tentativas
# 4 Bilhões de números, precisaria de, no máximo, 32 tentativas
# Sendo assim, conforme o número de itens cresce a pesquisa binária aumenta só um pouco
# seu tempo de execução, enquanto a pesquisa simples elevaria muito o mesmo.
#
#




# Recursão é quando uma função chama a si mesma. A recursão
# é utilizada para tornar a resposta mais clara.

# Devido ao fato de a função recursiva chamar a si mesma, é
# mais fácil de gerar erros e acabar em um loop infinito.

#Exemplo:

"""
def regressiva(i):
    print(i)
    regressiva(i-1)
"""
# Caso base e Caso recursivo

# Ao escrever uma função recursiva deve ser informado quando a recursão
# deve finalizar. O caso recursivo é quando a função chama a si mesma
# O caso base é quando a função não chama a si mesma novamente, de forma
# que não gere um loop infinito no código e finalize a execução do mesmo;

#def regressiva(i):
#    print(i)
#    if i <= 1:
#        return
#    else:
#        regressiva(i - 1)

#regressiva(10)

#Outro exemplo de função recursiva

def calcular_fatorial(n):                           # Cria a função calcular_fatorial(n) com n como parâmetro
    if n==0 or n==1:                                # Verifica se n é igaual a 0 ou um.
        return 1                                    # caso verdadeiro retorna 1
    return n * calcular_fatorial(n - 1)             # caso falso então multiplica a função calcular fatorial de n mas desta vez subtraindo 1

# Exemplo passo a passo para melhor compreensão
# :
# calcular_fatorial(5)
# if n==0 or n ==1:  Caso-base(interrompe a execução)  //Esta condicional retorna false então é ignorada
#    return 1
# return 5 * calcular_fatorial(4) //como a função ainda não possui o fatorial de 4 ela entrara em excução, então

# calcular_fatorial(4)
# if n==0 or n ==1:  //retorna false portanto é ignorada
#    return 1
# return 4 * calcular_fatorial(3)

# calcular_fatorial(3)
# if n==0 or n ==1:  //retorna false portanto é ignorada
#    return 1
# return 3 * calcular_fatorial(2)

# calcular_fatorial(2)
# if n==0 or n ==1:  //retorna false portanto é ignorada
#    return 1
# return 2 * calcular_fatorial(1)

# calcular_fatorial(1)
# if n==0 or n ==1:  //retorna true e interrompe a execução fazendo o processo reverso entao
#    return 1

# calcular_fatorial(2)
# if n==0 or n ==1:  //retorna false portanto é ignorada
#    return 1
# return 2 * 1 = 2

# calcular_fatorial(3)
# if n==0 or n ==1:  //retorna false portanto é ignorada
#    return 1
# return 3 * 2 = 6

# calcular_fatorial(4)
# if n==0 or n ==1:  //retorna false portanto é ignorada
#    return 1
# return 4 * 6 = 24

# calcular_fatorial(5)
# if n==0 or n ==1:
#    return 1
# return 5 * 4 = 120

# Portanto a função recebe chamadas recursivas até a obtensão de um caso-base
# e a partir do caso-base ela vem fazendo o processo inverso

print(calcular_fatorial(5))

# Exemplo:

array_de_numeros = [1,2,3]

# Para somar todos os números e retornar o valor total seria simples
# de ser feito porém, como seria feito com funções recursivas?

# PASSO 1: Descobrir o caso base. Qual seria o array mais simples que
# poderíamos obter? (um array com 0 ou 1 elementos)

# CasoBase:  [ ] -> 0 elementos a soma é igual a 0
#            [7] -> 1 elemento a soma é esse elemento (7)

# PASSO 2: A cada recursão, devemos chegar mais próximos do caso-base

def soma_recursiva(arr):
    if not arr:
        return 0

    return arr.pop(0) + soma_recursiva(arr)





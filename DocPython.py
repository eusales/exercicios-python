#--------------------------------------------------------------
# Declaração e atribuição de variáveis

    nome = "Juan"
    idade = 25
    altura = 1.75
    é estudante = True

    a = b = c = 10

# Regras para nomear variáveis

    # - Os nomes das variáveis só podem conter letras (a-z, A-Z), números (0-9) e sublinhados (_). Não podem começar com um número.

    # - O Python diferencia maiúsculas de minúsculas, então nome e Nome são variáveis diferentes.

    # - Não se pode usar palavras-chave reservadas do Python como nomes de variáveis (por exemplo, if, else, for, while, etc.).

    # - Recomenda-se usar nomes descritivos para as variáveis, que indiquem claramente seu propósito: nome, idade, total_vendas, etc.

    idade
    nome_completo
    total_vendas
    _contador

#--------------------------------------------------------------
# Tipos de dados basicos   

    #int (inteiros)

    idade = 25
    quantidade = 100

    #float (flutuante)

    preço = 2.99
    altura = 1.75

    #strings (cadeia de texto)

    nome = "Juan"
    mensagem = 'Olá, mundo'

    #Booleanos

    é_maior_de_idade = True
    tem_desconto = False

#--------------------------------------------------------------
# Operadores

    #Aritmétricos

    a = 10
    b = 3

    soma = a + b #13
    subtracao = a - b #7
    multiplicacao = a * b #30
    divisao = a / b #3.3333
    divisao_inteira = a // b #3
    modulo = a % b #1
    exponenciacao = a ** b #1000

    #Comparação

    a = 10
    b = 3

    igual = a == b   # False
    diferente = a != b   # True
    maior que = a > b   # True
    menor que = a < b   # False
    maior ou igual = a >= b   # True
    menor ou igual = a <= b   # False

    #Logico

    a = 10
    b = 3

    resultado_and = (a > 5) and (b < 5)   # True
    resultado_or = (a > 15) or (b < 5)   # True
    resultado_not = not (a > 5)   # False

#--------------------------------------------------------------
#Estruturas condicionais (Controle)

    #if

    idade = 18


    if idade >= 18:
    print ("Você é maior de idade.")

    #if-else

    idade = 15


    if idade >= 18:
    print ("Você é maior de idade.")

    else:
    print ("Você é menor de idade.")

    #if-elif-else

    nota = 85


    if nota >= 90:
    print ("Excelente")

    elif nota >= 80:
    print ("Muito bom")

    elif nota >= 70:
    print ("Bom")

    else:
    print ("Precisa melhorar")

#Loops

    #for

    frutas = ["maçã", "banana", "laranja"]


    for fruta in frutas:
        print(fruta)

    #While

    contador = 0


    while contador < 5:

        print(contador)
        contador += 1

    #Controle de loop

    #Break

    contador = 0


    while True:

        print(contador)
        contador += 1


        if contador == 5:
            break

    #Continue

    for i in range(10):

        if i % 2 == 0:
            continue
        print(i)

    #Pass

    for i in range(5):
        pass

#--------------------------------------------------------------
#Estruturas de dados

#Listas

    frutas = ["maçã", "banana", "laranja"]

    print(frutas[0])  # Imprime "maçã"
    print(frutas[1])  # Imprime "banana"
    print(frutas[2])  # Imprime "laranja"

        #a partir do final da lista utilizando índices negativos.

    print(frutas[-1])  # Imprime "laranja"
    print(frutas[-2])  # Imprime "banana"
    print(frutas[-3])  # Imprime "maçã"

    #Metodos de listas

    frutas = ["maçã", "banana", "laranja"]

    append(elemento): #adiciona um elemento ao final da lista.

    frutas.append("pera")
    print(frutas)  # Imprime ["maçã", "banana", "laranja", "pera"]
    #________________________________________________________
    insert(indice, elemento): #insere um elemento em uma posição específica da lista.
  
    frutas.insert(1, "uva")
    print(frutas)  # Imprime ["maçã", "uva", "banana", "laranja", "pera"]
    #________________________________________________________
    remove(elemento): #remove a primeira ocorrência de um elemento na lista.

    frutas.remove("banana")
    print(frutas)  # Imprime ["maçã", "uva", "laranja", "pera"]
    #________________________________________________________
    pop(indice): #remove e retorna o elemento em uma posição específica da lista.

    fruta_removida = frutas.pop(2)
    print(frutas)  # Imprime ["maçã", "uva", "pera"]
    print(fruta_removida)  # Imprime "laranja"
    #________________________________________________________
    sort(): #ordena os elementos da lista em ordem ascendente.

    frutas.sort()
    print(frutas)  # Imprime ["maçã", "pera", "uva"]
    #________________________________________________________
    reverse(): #inverte a ordem dos elementos na lista.

    frutas.reverse()
    print(frutas)  # Imprime ["uva", "pera", "maçã"]
    #________________________________________________________

    #Listas de compreensão

    números = [1, 2, 3, 4, 5]
    quadrados = [x ** 2 for x in números if x % 2 == 0]
    print(quadrados)  # Imprime [4, 16]

#_________________________________________________________________
#Tuplas

    ponto = (3, 4)

    print(ponto[0])  # Imprime 3
    print(ponto[1])  # Imprime 4

    #Métodos de tuplas       

    count(elemento): #devolve o número de vezes que um elemento aparece na tupla. 

        minha_tupla = (1, 2, 3, 2, 4, 2)
        contagem_do_dois = minha_tupla.count(2)
        print(f"O número 2 aparece {contagem_do_dois} vezes na tupla.") # Saída: O número 2 aparece 3 vezes na tupla.
    #_____________________________________________________________________________________________________________________________
    index(elemento): #devolve o índice da primeira aparição de um elemento na tupla. Opcionalmente, pode-se especificar o início e fim da busca.

        minha_tupla = (1, 2, 3, 2, 4, 2)

    print(f"A primeira ocorrência do 2 está no índice: {minha_tupla.index(2)}") # Saída: A primeira ocorrência do 2 está no índice: 1
    print(f"A primeira ocorrência do 2 a partir do índice 2 está no índice: {minha_tupla.index(2, 2)}") # Saída: A primeira ocorrência do 2 a partir do índice 2 está no índice: 3
    print(f"A primeira ocorrência do 2 entre os índices 2 e 4 (exclusivo) está no índice: {minha_tupla.index(2, 2, 4)}") # Saída: A primeira ocorrência do 2 entre os índices 2 e 4 (exclusivo) está no índice: 3
    #______________________________________________________________________________________________________________________________
    len(tupla): #embora não seja um método de tupla propriamente dito, esta função incorporada devolve o comprimento da tupla.

    minha_tupla = (1, 2, 3, 2, 4, 2)
    tamanho_da_tupla = len(minha_tupla)
    print(f"O tamanho da tupla é: {tamanho_da_tupla}") # Saída: O tamanho da tupla é: 6

#____________________________________________________________________________________________________________
#Dicionários

    pessoa = {"nome": "João", "idade": 25, "cidade": "Madri"}

    print(pessoa["nome"])  # Imprime "João"
    print(pessoa["idade"])    # Imprime 25
    print(pessoa["cidade"])  # Imprime "Madri"

    #Métodos de dicionários

    keys(): #retorna uma visualização de todas as chaves do dicionário.
    values(): #retorna uma visualização de todos os valores do dicionário.
    items(): #retorna uma visualização de todos os pares chave-valor do dicionário.
    update(outro_dicionario): #atualiza o dicionário com os pares chave-valor de outro dicionário.

    #____________________________________________________________________________________________________________
    pessoa = {"nome": "João", "idade": 25, "cidade": "Madri"}

    keys(): retorna uma visualização de todas as chaves do dicionário.
    print(pessoa.keys())    # Imprime dict_keys(["nome", "idade", "cidade"])
    print(pessoa.values())  # Imprime dict_values(["João", 25, "Madri"])
    print(pessoa.items())   # Imprime dict_items([("nome", "João"), ("idade", 25), ("cidade", "Madri")])


    pessoa.update({"profissao": "Engenheiro"})
    print(pessoa)  # Imprime {"nome": "João", "idade": 25, "cidade": "Madri", "profissao": "Engenheiro"}

#____________________________________________________________________________________________________________
#Conjuntos(set)

    frutas = {"maçã", "banana", "laranja"}
    numeros = set([1, 2, 3, 4, 5])

    conjunto1 = {1, 2, 3}
    conjunto2 = {3, 4, 5}


    uniao = conjunto1 | conjunto2
    print(uniao)  # Imprime {1, 2, 3, 4, 5}


    intersecao = conjunto1 & conjunto2
    print(intersecao)  # Imprime {3}


    diferenca = conjunto1 - conjunto2
    print(diferenca)  # Imprime {1, 2}


    diferenca_simetrica = conjunto1 ^ conjunto2
    print(diferenca_simetrica)  # Imprime {1, 2, 4, 5}

    #Métodos de conjuntos

    add(elemento): adiciona um elemento ao conjunto.
    remove(elemento): remove um elemento do conjunto. Se o elemento não existir, gera um erro.
    discard(elemento): remove um elemento do conjunto se estiver presente. Se o elemento não existir, não faz nada.
    clear(): remove todos os elementos do conjunto.

    #Exemplo:

    frutas = {"maçã", "banana", "laranja"}


    frutas.add("pera")
    print(frutas)  # Imprime {"maçã", "banana", "laranja", "pera"}


    frutas.remove("banana")
    print(frutas)  # Imprime {"maçã", "laranja", "pera"}


    frutas.discard("uva")
    print(frutas)  # Imprime {"maçã", "laranja", "pera"}


    frutas.clear()
    print(frutas)  # Imprime set()

#_________________________________________________________________________________________________________
#Funções

    # Definição e chamada de funções

    def saudacao():
    print("Olá, mundo!")


    saudacao()  # Imprime "Olá, mundo!"

    #Parâmetros e argumentos

    def saudacao(nome):
    print(f"Olá, {nome}!")

    saudacao("João")  # Imprime "Olá, João!"
    saudacao("Maria")  # Imprime "Olá, Maria!"

    # Valores de retorno

    def soma(a, b):
    return a + b

    resultado = soma(3, 4)
    print(resultado)  # Imprime 7

    # Funções anônimas (lambda)

    quadrado = lambda x: x ** 2
    print(quadrado(5))  # Imprime 25

    # Escopo das variáveis (local vs. global)

    def funcao():
    variavel_local = 10
    print(variavel_local)  # Acessível dentro da função

    variavel_global = 20

    def funcao2():
        print(variavel_global)  # Acessível de qualquer lugar

    funcao()  # Imprime 10
    funcao2()  # Imprime 20
    print(variavel_global)  # Imprime 20
    print(variavel_local)  # Gera um erro, a variável não está definida neste escopo.

    # Funções definidas pelo usuário

        # Documentação de funções (docstrings)
        def area_retangulo(base, altura):
        """
            Calcula a área de um retângulo.


            Args:
                base (float): A base do retângulo.
                altura (float): A altura do retângulo.


            Returns:
                float: A área do retângulo.
            """
            return base * altura

        # Funções com número variável de argumentos

        def soma_variavel(*numeros):
            total = 0
            for numero in numeros:
                total += numero
        return total


        print(soma_variavel(1, 2, 3))  # Imprime 6
        print(soma_variavel(4, 5, 6, 7))  # Imprime 22

#_________________________________________________________________________________________________________
# Erros comuns em Python

    # Erro de sintaxe (SyntaxError)
    # - Ocorre quando o código não segue as regras de sintaxe do Python, como esquecer dois pontos após uma declaração de função ou um loop.

    # Erro de nome (NameError)
    # - Ocorre quando se faz referência a uma variável ou função que não foi definida.

    # Erro de tipo (TypeError)
    # - Ocorre quando se realiza uma operação com tipos de dados in 

    # Erro de índice (IndexError)
    # - Ocorre quando se tenta acessar um índice fora do intervalo válido de uma lista ou sequência.

#_________________________________________________________________________________________________________
# Manejo de exceções

# Try

    # O bloco try contém o código que pode gerar uma exceção. Se ocorrer uma exceção dentro do bloco try, o fluxo de execução é transferido para o bloco except correspondente.

    try:
        # Código que pode gerar uma exceção
        resultado = 10 / 0  # Divisão por zero
        print(resultado)
    except ZeroDivisionError:
        print("Erro: Divisão por zero")

#Except

    # O bloco except especifica o tipo de exceção que se deseja capturar e lidar. Você pode ter múltiplos blocos except para lidar com diferentes tipos de exceções.

    try:
        # Código que pode gerar uma exceção
        resultado = 10 / 0  # Divisão por zero
        print(resultado)
    except ZeroDivisionError:
        print("Erro: Divisão por zero")
    except ValueError:
        print("Erro: Valor inválido")

#Finally

    # O bloco finally é opcional e é executado sempre, independentemente de ter ocorrido uma exceção ou não. É comumente utilizado para realizar tarefas de limpeza ou liberação de recursos.

    try:
        # Código que pode gerar uma exceção
        arquivo = open("arquivo.txt", "r")
        # Realizar operações com o arquivo
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado")
    finally:
        arquivo.close()  # Fechar o arquivo sempre, mesmo se ocorrer uma exceção
    
#_________________________________________________________________________________________________________
# Exceções personalizadas
    
    # Exemplo

    def funcao():
    # Código que pode gerar uma exceção personalizada
    if condicao:
        raise Exception("Descrição do erro")

    try:
        funcao()
    except Exception as e:
        print(f"Erro: {str(e)}")

#_________________________________________________________________________________________________________
# Entradas/saídas

    nome = input("Insira seu nome: ")
    idade = input("Insira sua idade: ")

    print("Olá, " + nome + "!")
    print("Você tem " + idade + " anos.")

    # funções como int() ou float()

    idade = int(input("Insira sua idade: "))

    if idade >= 18:
        print("Você é maior de idade.")
    else:
        print("Você é menor de idade.")

# Saída de dados

    nome = "Juan"
    idade = 25

    print(f"Olá, meu nome é {nome} e tenho {idade} anos.")

#_________________________________________________________________________________________________________
# Leitura de arquivos
# - devemos abri-lo utilizando a função open() em modo de leitura ("r"). Depois, podemos ler o conteúdo do arquivo utilizando métodos como read() ou readlines().

    arquivo = open("dados.txt", "r")
    conteudo = arquivo.read()
    print(conteudo)
    arquivo.close()

# Escrita de arquivos
# - abrimos em modo de escrita ("w") utilizando a função open(). Se o arquivo não existir, será criado automaticamente. Se o arquivo já existir, seu conteúdo será sobrescrito.

    arquivo = open("dados.txt", "w")
    arquivo.write("Olá, mundo!")
    arquivo.close()

# Você também pode utilizar a declaração with para manejar a abertura e fechamento de arquivos de maneira automática.

    with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# Atenção; É importante fechar sempre os arquivos depois de utilizá-los para liberar os recursos do sistema. 

#_________________________________________________________________________________________________________
# Importar módulos
    import math

    resultado = math.sqrt(25)
    print(resultado)  # Imprime 5.0

    # Também podemos importar funções específicas de um módulo utilizando a sintaxe from módulo import função.

    from math import sqrt


    resultado = sqrt(25)
    print(resultado)  # Imprime 5.0

# Funções e classes de módulos padrão

    # Math - Fornece funções matemáticas, como sqrt() (raiz quadrada), sin() (seno), cos() (cosseno), entre outras.
    # Random - Oferece funções para gerar números aleatórios, como random() (número aleatório entre 0 e 1), randint() (número inteiro aleatório em um intervalo), entre outras.
    # Datatime - Permite trabalhar com datas e horas, como datetime.now() (data e hora atual), datetime.date() (data), datetime.time() (hora), entre outras.

    import random
    import datetime

    numero_aleatorio = random.randint(1, 10)
    print(numero_aleatório)  # Imprime um número inteiro aleatório entre 1 e 10

    data_atual = datetime.datetime.now()
    print(data_atual)  # Imprime a data e hora atual

# Existem varios tipos de modulo

#_________________________________________________________________________________________________________
# Criar e utilizar módulos personalizados

    #meu_modulo.py
    def saudar(nome):
        print(f"Olá, {nome}!")


    def calcular_soma(a, b):
        return a + b

# Depois, podemos importar e utilizar as funções definidas em meu_modulo.py em outro arquivo Python.

    import meu_modulo

    meu_modulo.saudar("João")  # Imprime "Olá, João!"
    resultado = meu_modulo.calcular_soma(5, 3)
    print(resultado)  # Imprime 8

# Organização do código em módulos

    # operacoes.py
    def somar(a, b):
        return a + b


    def subtrair(a, b):
        return a - b


    # utilidades.py
    def imprimir_mensagem(mensagem):
        print(mensagem)


    def obter_nome_usuario():
        return input("Digite seu nome: ")

# Depois, podemos importar e utilizar essas funções em nosso programa principal.

    import operacoes
    import utilidades


    resultado = operacoes.somar(5, 3)
    utilidades.imprimir_mensagem(f"O resultado da soma é: {resultado}")


    nome = utilidades.obter_nome_usuario()
    utilidades.imprimir_mensagem(f"Olá, {nome}!")
#_________________________________________________________________________________________________________
# Criar e utilizar pacotes
    # Para criar um pacote, criamos um diretório com o nome desejado e adicionamos um arquivo especial chamado __init__.py dentro do diretório. Este arquivo pode estar vazio ou conter código de inicialização do pacote.
    # or exemplo, criamos um diretório chamado meu_pacote com a seguinte estrutura:

        meu_pacote/
        __init__.py
        modulo1.py
        modulo2.py

    # Depois, podemos importar e utilizar os módulos do pacote em nosso programa. 

        from meu_pacote import modulo1, modulo2

        modulo1.funcao1()
        modulo2.funcao2()

#_________________________________________________________________________________________________________

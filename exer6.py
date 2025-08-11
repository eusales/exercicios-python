"""
Exercício 6: Encontrar o Anagrama Mais Longo
Crie um programa que leia um arquivo de texto (.txt) contendo uma lista de palavras (uma por linha). O objetivo é encontrar o grupo de palavras que são anagramas umas das outras e que, juntas, formam o anagrama mais longo.

Um anagrama é uma palavra formada pela reordenação das letras de outra palavra. Por exemplo, "amor" e "roma" são anagramas.

O que o programa deve fazer:

- Ler o arquivo de texto com a lista de palavras.

- Agrupar as palavras que são anagramas. A maneira mais comum de fazer isso é criando uma "chave" para cada palavra. Por exemplo, você pode ordenar as letras de cada palavra ("amor" e "roma" se tornariam "amor") e usar essa string ordenada como chave para um dicionário.

- Encontrar o grupo de anagramas mais longo. Ou seja, o grupo que contém o maior número de palavras.

- Imprimir o resultado: O programa deve imprimir o grupo de palavras que formam o anagrama mais longo e a quantidade de palavras neste grupo.
"""

from collections import defaultdict

def encontrar_anagrama_mais_longo(nome_arquivo):
    """
    Lê um arquivo de texto e encontra o grupo de anagramas mais longo.

    Args:
        nome_arquivo (str): O nome do arquivo de texto com uma palavra por linha.
    """
    grupos_de_anagramas = defaultdict(list)

    # 1. Lê o arquivo e agrupa as palavras
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                palavra = linha.strip().lower()  # Remove espaços e converte para minúsculas
                if not palavra:
                    continue  # Pula linhas vazias

                # Cria a chave do anagrama ordenando as letras
                chave = "".join(sorted(palavra))
                
                # Adiciona a palavra original ao grupo correspondente
                grupos_de_anagramas[chave].append(palavra)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return

    # 2. Encontra o grupo de anagramas mais longo
    grupo_mais_longo = []
    
    for chave in grupos_de_anagramas:
        if len(grupos_de_anagramas[chave]) > len(grupo_mais_longo):
            grupo_mais_longo = grupos_de_anagramas[chave]

    # 3. Imprime o resultado
    if grupo_mais_longo:
        print("O grupo de anagramas mais longo é:")
        print(grupo_mais_longo)
        print(f"Quantidade de palavras: {len(grupo_mais_longo)}")
    else:
        print("Nenhum grupo de anagramas encontrado.")
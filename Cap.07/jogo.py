# Projeto 1 - desenvolvimento de Game em Linguagem Python - versão 1

# Import
import random
from os import system, name

# Funcão para limar a tela a cada execução

def limpa_tela():
    # windons
    if name == 'nt':
        _ = system('cls')

    #Mac ou Linux
    else:
        _ = system('clear')

# Função
def game():

    limpa_tela()
    print("\nBem-vindo(a) ao jogo da froca!")
    print("Adivinhe a palavra:\n")

    # Lista de palavras para o jogo
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']

    # Escolher randomicamente uma palavra
    palavra = random.choice(palavras)

    # List comprehension
    letras_descobertas = ['_'for letra in palavra]

    # Número de chances
    chances = 6

    # Lista para as letras erradas
    letras_erradas = []

    #Loop enquanto número de chances for maior do que zero
    while chances > 0:

        #print
        print(" ".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("Letras erradas:", " ".join(letras_erradas))

        #tentativa
        tentativa = input("\nDigite uma letra: ").lower()

        #Condicional
        if tentativa in palavra:
            index = 0

            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)
        
        #Condicional
        if "_" not in letras_descobertas:
            print("\nVocê venceu, a palavra era:", palavra)
            break

    # Condicional
    if "_" in letras_descobertas:
        print("\nVocê perdeu, a palavra era:", palavra)

# Bloco main
if __name__ == "__main__":
    game()
    print("\nParabéns, Você é um otátio. >:P\n")


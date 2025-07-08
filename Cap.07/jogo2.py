# Projeto 1 - desenvolvimento de Game em Linguagem Python - versão 1

import random
from os import system, name

def limpa_tela():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def display_hangman(chances):
    stages = [
        """
            __________
            |        |
            |        O
            |       \\|/
            |        |
            |       / \\
            -
        """,
        """
            __________
            |        |
            |        O
            |       \\|/
            |        |
            |       /
            -
        """,
        """
            __________
            |        |
            |        O
            |       \\|/
            |        |
            |
            -
        """,
        """
            __________
            |        |
            |        O
            |       \\|
            |        |
            |
            -
        """,
        """
            __________
            |        |
            |        O
            |        |
            |        |
            |
            -
        """,
        """
            __________
            |        |
            |        O
            |        
            |        
            |
            -
        """,
        """
            __________
            |        |
            |        
            |        
            |        
            |
            -
        """
    ]
    return stages[chances]

def game():
    limpa_tela()
    print("\nBem-vindo(a) ao jogo da forca!")
    print("Adivinhe a palavra:\n")

    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']
    palavra = random.choice(palavras)
    tabuleiro = ["_"] * len(palavra)
    chances = 6
    letras_erradas = []
    letras_tentadas = []

    while chances > 0:
        print(display_hangman(chances))
        print("Palavra:", " ".join(tabuleiro))
        print("Chances restantes:", chances)
        print("Letras erradas:", " ".join(letras_erradas))

        tentativa = input("\nDigite uma letra: ").lower()

        if not tentativa.isalpha() or len(tentativa) != 1:
            print("Digite apenas uma letra válida!")
            continue

        if tentativa in letras_tentadas:
            print("Você já tentou essa letra.")
            continue

        letras_tentadas.append(tentativa)

        if tentativa in palavra:
            for idx, letra in enumerate(palavra):
                if letra == tentativa:
                    tabuleiro[idx] = letra
        else:
            chances -= 1
            letras_erradas.append(tentativa)

        if "_" not in tabuleiro:
            print("\nParabéns, você venceu! A palavra era:", palavra)
            break

    if "_" in tabuleiro:
        print(display_hangman(chances))
        print("\nVocê perdeu, a palavra era:", palavra)

if __name__ == "__main__":
    game()


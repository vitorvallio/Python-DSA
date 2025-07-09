import random

# Hangman Game (Jogo da Forca) - Orientação a Objetos
# ---------------------------------------------------
# Neste script, implementamos o clássico jogo da forca usando uma classe
# que encapsula todo o comportamento e estado do jogo.

# Tabuleiro de desenho da forca em diferentes estágios de erro
BOARD = [
    '''
    +---+
    |   |
        |
        |
        |
        |
    =======''',
    '''
    +---+
    |   |
    O   |
        |
        |
        |
    =======''',
    '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =======''',
    '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =======''',
    '''
    +---+
    |   |
    O   |
   /|\\  |
        |
        |
    =======''',
    '''
    +---+
    |   |
    O   |
   /|\\  |
   /    |
        |
    =======''',
    '''
    +---+
    |   |
    O   |
   /|\\  |
   / \\  |
        |
    ======='''
]

class Hangman:
    """
    Classe Hangman encapsula o estado e o comportamento do jogo da forca.

    Atributos:
        word (str): palavra secreta a ser adivinhada
        board (list): arte ASCII da forca em diferentes estágios
        guessed_letters (set): letras já chutadas corretamente
        wrong_letters (set): letras chutadas incorretamente
        max_errors (int): número máximo de erros permitido
    Métodos:
        __init__: inicializa o jogo com uma palavra aleatória
        guess(letter): processa um palpite do jogador
        is_finished(): verifica se o jogo terminou (venceu ou perdeu)
        is_won(): retorna True se o jogador venceu
        print_status(): exibe o tabuleiro e estado atual do jogo
    """

    def __init__(self, word_list, max_errors=2):
        # Seleciona aleatoriamente a palavra secreta
        self.word = random.choice(word_list).lower()
        # Inicializa coleções de letras chutadas
        self.guessed_letters = set()
        self.wrong_letters = set()
        # Estado de tentativas
        self.max_errors = max_errors

    def guess(self, letter):
        """
        Recebe um palpite (uma letra) e atualiza o estado do jogo.
        Retorna True se a letra estiver na palavra, False caso contrário.
        """
        letter = letter.lower()
        if not letter.isalpha() or len(letter) != 1:
            raise ValueError("Digite apenas uma letra válida.")
        if letter in self.guessed_letters or letter in self.wrong_letters:
            return None  # letra já tentada

        if letter in self.word:
            self.guessed_letters.add(letter)
            return True
        else:
            self.wrong_letters.add(letter)
            return False

    def is_finished(self):
        """
        Retorna True se o jogo terminou (venceu ou perdeu).
        """
        return self.is_won() or len(self.wrong_letters) >= self.max_errors

    def is_won(self):
        """
        Verifica se o jogador conseguiu adivinhar todas as letras.
        """
        return all(ch in self.guessed_letters for ch in self.word)

    def print_status(self):
        """
        Exibe o tabuleiro atual, as letras chutadas e o progresso.
        """
        # Desenha a forca de acordo com o número de erros
        errors = len(self.wrong_letters)
        print(BOARD[errors])
        print()
        # Exibe a palavra com letras reveladas e '_' para não reveladas
        display = [ch if ch in self.guessed_letters else '_' for ch in self.word]
        print("Palavra: ", ' '.join(display))
        print(f"Erros ({errors}/{self.max_errors}): ", ' '.join(sorted(self.wrong_letters)))

if __name__ == "__main__":
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']
    jogo = Hangman(palavras)

    print("\nBem-vindo(a) ao Jogo da Forca!\n")
    while not jogo.is_finished():
        jogo.print_status()
        try:
            palpite = input("\nDigite uma letra: ")
            res = jogo.guess(palpite)
            if res is True:
                print("\n✅ Letra correta!\n")
            elif res is False:
                print("\n❌ Letra incorreta.\n")
            else:
                print("\n⚠️  Você já tentou essa letra.\n")
        except ValueError as ve:
            print(f"\n⚠️  {ve}\n")

    # Exibe resultado final
    jogo.print_status()
    if jogo.is_won():
        print("\n🎉 Parabéns seu noia, você venceu!\n")
    else:
        print(f"\n💀 Você perdeu. A palavra era '{jogo.word}'.\n")
class JeuDuPendu:
    def __init__(self, word_to_find: str, tries: int):
        self.word_to_find = [*word_to_find.upper()]
        self.hidden_word = ["_"] * len(word_to_find)
        self.guesses = []
        self.tries = tries

    def run(self):
        while True:
            print(self.print_word())

            if self.is_word_found():
                print("Vous avez gagner !")
                break

            print(f'Vous avez encore {self.tries} tentatives.')
            self.make_guess()

            if not self.is_new_letter_found():
                self.tries -= 1
                if self.tries == 0:
                    print(self.print_word(True))
                    print('Vous avez perdu.')
                    break

    def make_guess(self):
        while True:
            print('')
            guess = input('Votre réponse : ').upper()
            if len(guess) != 1:
                print('Merci d\'entrer un seul caractère.')
            elif guess in self.guesses:
                print(f'Vous avez déjà entrer la lettre "{guess}".')
            else:
                self.guesses.append(guess)
                break

    def is_new_letter_found(self):
        valid_guess = False
        for i in range(len(self.word_to_find)):
            if self.word_to_find[i] in self.guesses:
                if self.hidden_word[i] == '_':
                    valid_guess = True
                    self.hidden_word[i] = self.word_to_find[i]
        return valid_guess

    def print_word(self, show_word=False):
        word = ''
        letters = self.word_to_find if show_word else self.hidden_word
        for letter in letters:
            word = word + ' ' + letter
        return word

    def is_word_found(self):
        return self.hidden_word == self.word_to_find


JeuDuPendu('ACCOMPLI', 2).run()

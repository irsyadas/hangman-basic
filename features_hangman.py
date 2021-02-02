import random

class Features:
    def words(self):
        with open('wordlist.txt','r') as f:
            self.words_list = [line.strip() for line in f]
            return self.words_list

    def guess(self):
        self.guess_word = random.choice(self.words_list).lower()
        return self.guess_word

    def letter(self):
        self.word_len = len(self.guess_word)
        return self.word_len

    def game_over(self):
        self.game_over = False

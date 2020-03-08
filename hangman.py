
# -*- coding: utf-8 -*-

#
#   hangman.py
#
#   A simple Hangman game
#
#   Author: Raphael Monte <raphaeldetarso@gmail.com>
#
#   Update the list of words in words.txt
#   Initiate the game with hangman = Hangman()
#


# Import libs
import random


class Hangman(object):

    # Initiate the game
    def __init__(self):
        self.missed_letters = []
        self.guessed_letters = []
        self.word = self.rand_word()
        self.man = ['0', '|', '/', '\\', '/', '\\']

        while not self.endgame():
            self.print_game()

    # Verify if the game is end
    def endgame(self):
        if len(self.missed_letters) == 6:
            print(50 * '=')
            print('Você perdeu otário!')
            print('A palavra correta é: ', self.word)
            print(50 * '=')

            return True
        elif len(self.guessed_letters) == len(self.word):
            print(50 * '=')
            print('VOCÊ GANHOU!')
            print('A palavra é: ', self.word)
            print(50 * '=')
            return True
        else:
            return False

    # Ask the letter
    def get_letter(self):
        letter = input('Informe uma letra: ')

        # Verify if the letter is correct
        if letter in self.word:
            self.guessed_letters.append(letter)
        else:
            self.missed_letters.append(letter)

    # return the spaces and the corrected letters
    def get_word_spaces(self):
        word_spaces = 'Palavra: '
        for letter in self.word:
            if letter in self.guessed_letters:
                word_spaces += letter
            else:
                word_spaces += ' _ '
        return word_spaces

    # initiate new round
    def print_game(self):
        body = self.body(len(self.missed_letters))
        print(self.board(body))
        print(self.get_word_spaces())
        self.get_letter()

    # return the body of the handman
    def body(self, points):
        body = []
        for i in range(len(self.man)):
            if points > i:
                body.insert(i, self.man[i])
            else:
                body.insert(i, ' ')
        return body

    # return the board
    def board(self, body):
        board = ('-' * 10) + ' Hangman ' + ('-' * 10)
        board = '''
            +------+
            |      |
            |      {0}
            |     {2}{1}{3}
            |     {4} {5}
            |
        _ _ |_ _ _
        '''.format(body[0], body[1], body[2], body[3], body[4], body[5])

        return board

    # return a random word
    def rand_word(self):
        with open("words.txt", "rt") as f:
            bank = f.readlines()
        return bank[random.randint(0, len(bank) - 1)].strip()

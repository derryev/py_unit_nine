import random


class Colors:
    # from https://www.geeksforgeeks.org/print-colors-python-terminal/
    ''' Colors class:reset all colors with colors.reset; two
    subclasses fg for foreground
    and bg for background; use as colors.subclass.colorname.
    i.e. colors.fg.red or colors.bg.green also, the generic bold, disable,
    underline, reverse, strike through,
    and invisible work with the main class i.e. colors.bold '''
    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m'

    class Fg:
        black = '\033[30m'
        red = '\033[31m'


class Deck:
    def __init__(self):
        self.card_deck = []
        self.ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.suits = {'♣', '♦', '♥', '♠'}
        self.cards = []
        # got from chat gtp/demetri
        for suit in self.suits:
            for rank in self.ranks:
                card = {'rank': rank, 'suit': suit}
                self.card_deck.append(card)

    def shuffle_deck(self):
        # got from https://www.globaltechcouncil.org/python/how-to-make-a-deck-of-cards-with-python/
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def show_deck(self):
        print(self.card_deck)
    # self.card_deck.append(card)


deck1 = Deck()
deck1.show_deck()

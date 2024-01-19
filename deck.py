import random


class Colors:
    # the website https://levelup.gitconnected.com/how-to-print-in-color-in-python-without-external-libraries-db6e15e5c03c
    # helped me figure out how to implement the color codes in the program using the "+"
    BOLD = "\033[1m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    RESET = "\033[0m"


class Deck:
    def __init__(self):
        self.card_deck = []
        self.ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.suits = {'♣', Colors.RED+'♦'+Colors.RESET, Colors.RED+'♥'+Colors.RESET, '♠'}
        self.p1_cards = []
        self.p2_cards = []
        # got from chat gtp/demetri
        for suit in self.suits:
            for rank in self.ranks:
                card = {'rank': rank, 'suit': suit}
                self.card_deck.append(card)

    def shuffle_deck(self):
        # got from https://www.scaler.com/topics/python-shuffle-list/
        n = len(self.card_deck)
        for i in range(n - 1, 0, -1):
            j = random.randint(0, i + 1)
            self.card_deck[i], self.card_deck[j] = self.card_deck[j], self.card_deck[i]

    def show_deck(self):
        print(self.card_deck)

    # def deal_cards_p1(self, specific_deck, number_to_deal):
    #     self.p1_cards = specific_deck[0, (number_to_deal-1)]
    #     return self.p1_cards
    #
    # def deal_cards_p2(self, specific_deck, number_to_deal):
    #     self.p2_cards = specific_deck[number_to_deal, (number_to_deal + number_to_deal)]
    #     return self.p2_cards

    def deal_cards(self, number_to_deal):
        # got information on how to randomly choose a card to add to the hand from https://www.youtube.com/watch?v=xrNmP_dCaGY
        for x in range(number_to_deal):
            card = random.choice(self.card_deck)
            self.card_deck.remove(card)
            self.p1_cards.append(card)
        for x in range(number_to_deal):
            card = random.choice(self.card_deck)
            self.card_deck.remove(card)
            self.p2_cards.append(card)





# deck1 = Deck()
# deck1.show_deck()
# deck1.shuffle_deck()
# deck1.show_deck()

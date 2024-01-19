import random


class Colors:
    # https://levelup.gitconnected.com/how-to-print-in-color-in-python-without-external-libraries-db6e15e5c03c helped me
    # figure out how to implement the color codes in the program using the "+"
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
        # Figured out how to use the nested for loop to create a deck of cards with help from Demetri's ChatGTP
        for suit in self.suits:
            for rank in self.ranks:
                card = {'rank': rank, 'suit': suit}
                self.card_deck.append(card)

    def shuffle_deck(self):
        """
        Uses the fisher yates shuffle algorithm to shuffle the instance of the deck of cards
        :return: nothing
        """
        # Learned how to write the fisher-yates shuffle algorithm
        # from https://www.scaler.com/topics/python-shuffle-list/
        n = len(self.card_deck)
        for i in range(n - 1, 0, -1):
            j = random.randint(0, i + 1)
            self.card_deck[i], self.card_deck[j] = self.card_deck[j], self.card_deck[i]

    def show_deck(self):
        """
        Prints the card deck dictionary.
        :return: nothing
        """
        print(self.card_deck)

    def deal_cards(self, number_to_deal):
        """
        with a for loop for each player, a number of random cards based on how many cards the user wanted to be dealt
        are removed from the deck and added to each player's hand.
        :param number_to_deal: the number of cards the user wants dealt to each player (int)
        :return: nothing
        """
        # I got information on how to randomly choose a card to add to the hand from
        # https://www.youtube.com/watch?v=xrNmP_dCaGY, which taught me about random.choice
        for x in range(number_to_deal):
            card = random.choice(self.card_deck)
            self.card_deck.remove(card)
            self.p1_cards.append(card)
        for x in range(number_to_deal):
            card = random.choice(self.card_deck)
            self.card_deck.remove(card)
            self.p2_cards.append(card)

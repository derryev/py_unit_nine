# Eva D
# Jan 18 2024
# Plays simulation of card game compare with two players.

from deck import Deck
from deck import Colors


def welcome_player():
    """
    Welcomes the player with two print statements welcoming the user and explaining how the game works.
    :return: nothing
    """
    print("Welcome to the game of compare. You will decide how many cards we get and then we'll play them one by one.")
    print("Whoever has the higher card wins that round. Whoever wins the most rounds wins the game.")


def create_shuffled_card_deck(deck_of_cards):
    """
    shuffles the instance of the Deck class using the shuffle_deck method, which employs the fisher-yates shuffle
    algorithm
    :param deck_of_cards: this is an instance of the Deck class, which will then be shuffled
    :return: the shuffled instance of the deck of cards (instance of a class)
    """
    deck_of_cards.shuffle_deck()
    return deck_of_cards


def get_input_on_card_number():
    """
    gets user input on the number of cards to deal to each player, ensuring that this number is a digit between 1-26
    :return: the number of cards the user wants dealt to each player (int)
    """
    while True:
        number_cards_deal = input("How many cards should each player get? Enter a number between 1 and 26: ")
        # this while loop ensures that the input given is a numerical digit and is between 1 and 26
        if number_cards_deal.isdigit() is False or number_cards_deal.isdecimal() is False:
            print("Invalid input. Please enter a number between 1 and 26.")
        elif float(number_cards_deal) < 1 or float(number_cards_deal) > 26:
            print("Invalid input. Please enter a number between 1 and 26.")
        else:
            return int(number_cards_deal)


def deal_cards(card_deck, number_to_deal):
    """
    uses the card_deck instance and the number of cards the user wants dealt with the deal_cards method to deal a
    certain number of cards to each player (storing them in a self variable for each user). Also prints out each user's
    hand based on the cards that were just dealt and using the self variables the card lists were stored in.
    :param card_deck: the shuffled instance of the Deck class, which is the card deck in use for this game
    :param number_to_deal: the number of cards the user wants dealt to each player (int)
    :return: nothing
    """
    if number_to_deal == 1:
        print("Dealer deals "+str(number_to_deal)+" card to each player...")
    else:
        print("Dealer deals " + str(number_to_deal) + " cards to each player...")
    print("")
    # uses the deal_cards method to deal a certain number of cards to each user based on what the user requested
    card_deck.deal_cards(number_to_deal)
    # this creates a list of each player's hand, which is then joined, to give output of the cards that each player has
    p1_hand_list = []
    p2_hand_list = []
    for x in range(number_to_deal):
        p1_card = card_deck.p1_cards[x]
        p2_card = card_deck.p2_cards[x]
        p1_hand_list.append(str(p1_card['rank'])+str(p1_card['suit']))
        p2_hand_list.append(str(p2_card['rank']) + str(p2_card['suit']))
    print("Player 1 Hand: "+" ".join(p1_hand_list))
    print("Player 2 Hand: " + " ".join(p2_hand_list))


def play_round(deck_of_cards, number_to_deal):
    """
    plays out all the rounds of the game by printing out the necessary output (which round, which cards, who wins)
    based on what the compare_cards function returns, keeping count of who wins each round, and finally determining the
    winner of the game, returning True, False, or "Tie" to signify who wins.
    :param deck_of_cards: the shuffled instance of the deck_of_cards class so that the self variables with each player's
    dealt cards can be used.
    :param number_to_deal: the number of cards each player has, which will determine how many rounds play (int)
    :return: Either True, False, or "Tie", which signifies that P1, P2, or neither player won overall respectively.
    """
    p1_point_counter = 0
    p2_point_counter = 0
    # the for loop runs the rounds a certain number of times based on how many cards each player has, comparing the
    # cards and keeping count of who wins each round with a point counter
    for x in range(0, number_to_deal):
        print("")
        p1_card = deck_of_cards.p1_cards[x]
        p2_card = deck_of_cards.p2_cards[x]
        round_number = x+1
        if compare_cards(p1_card, p2_card, round_number) is True:
            print("Player 1 wins this round!")
            p1_point_counter = p1_point_counter + 1
        else:
            print("Player 2 wins this round!")
            p2_point_counter = p2_point_counter + 1
    print("")
    print(Colors.BOLD+"Game over!"+Colors.RESET)
    # specifies language of output based on if the points earned are plural or not
    if p1_point_counter == 1:
        print("Player 1 wins:", p1_point_counter, "round")
    else:
        print("Player 1 wins:", p1_point_counter, "rounds")
    if p2_point_counter == 1:
        print("Player 2 wins:", p2_point_counter, "round")
    else:
        print("Player 2 wins:", p2_point_counter, "rounds")
    # returns a value based on who won the most points, True for P1, False for P2, and "Tie" if they tied
    if p1_point_counter > p2_point_counter:
        return True
    elif p1_point_counter < p2_point_counter:
        return False
    else:
        return "Tie"


def compare_cards(p1_card, p2_card, round_number):
    """
    Compares the cards each player has in every round, determining who has the higher card based on their list index
    value in rank and suit if needed, returning either True or False to signify who won the individual round.
    :param p1_card: The card that P1 is playing in this specific round. (dictionary item)
    :param p2_card: The card that P1 is playing in this specific round. (dictionary item)
    :param round_number: the number of the round, which will allow for appropriate output statements on what round it
    is (int)
    :return: True or False based on if P1 or P2 had a higher value card respectively.
    """
    ranks_list = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suits_list = ['♣', Colors.RED+'♦'+Colors.RESET, Colors.RED+'♥'+Colors.RESET, '♠']
    print(Colors.BOLD+"Round "+str(round_number)+":"+Colors.RESET)
    print("Player 1:", p1_card['rank'], "of", p1_card['suit'])
    print("Player 2:", p2_card['rank'], "of", p2_card['suit'])
    # learned how to index items in a list from Demetri, and altered parts of the code he posted to work with my program
    # if p1's card is a greater rank than p2's, it will return true
    if p1_card['rank'] == p2_card['rank']:
        if suits_list.index(p1_card['suit']) > suits_list.index(p2_card['suit']):
            return True
        else:
            return False
    else:
        if ranks_list.index(p1_card['rank']) > ranks_list.index(p2_card['rank']):
            return True
        else:
            return False


def main():
    # creates an instance of the deck of cards class
    deck_of_cards = Deck()
    welcome_player()
    create_shuffled_card_deck(deck_of_cards)
    number_to_deal = get_input_on_card_number()
    deal_cards(deck_of_cards, number_to_deal)
    # assigns a value of True, False, or Tie to a variable based on who won the most rounds in the card game
    winner = play_round(deck_of_cards, number_to_deal)
    # gives final output based on what the last function returned to show the winner to the user
    if winner is True:
        print(Colors.GREEN+"Player 1 wins the game!"+Colors.RESET)
    elif winner is False:
        print(Colors.GREEN+"Player 2 wins the game!"+Colors.RESET)
    else:
        print("It's a tie!")


main()

# Eva D
# Jan 18 2024
# Plays simulation of card game compare with two players.

from deck import Deck
from deck import Colors


def welcome_player():
    print("Welcome to the game of compare. You will decide how many cards we get and then we'll play them one by one.")
    print("Whoever has the higher card wins that round. Whoever wins the most rounds wins the game.")


def create_shuffled_card_deck(deck_of_cards):
    # deck_of_cards.show_deck()
    deck_of_cards.shuffle_deck()
    # deck_of_cards.show_deck()
    return deck_of_cards
    # card_deck.show_deck()


def get_input_on_card_number():
    while True:
        number_cards_deal = input("How many cards should each player get? Enter a number between 1 and 26: ")
        if number_cards_deal.isdigit() is False or number_cards_deal.isdecimal() is False:
            print("Invalid input. Please enter a number between 1 and 26.")
        elif float(number_cards_deal) < 1 or float(number_cards_deal) > 26:
            print("Invalid input. Please enter a number between 1 and 26.")
        else:
            return int(number_cards_deal)


def deal_cards(card_deck, number_to_deal):
    if number_to_deal == 1:
        print("Dealer deals "+str(number_to_deal)+" card to each player...")
    else:
        print("Dealer deals " + str(number_to_deal) + " cards to each player...")
    print("")
    card_deck.deal_cards(number_to_deal)
    p1_hand_list = []
    p2_hand_list = []
    for x in range(number_to_deal):
        p1_card = card_deck.p1_cards[x]
        p2_card = card_deck.p2_cards[x]
        p1_hand_list.append(str(p1_card['rank'])+str(p1_card['suit']))
        p2_hand_list.append(str(p2_card['rank']) + str(p2_card['suit']))
    print("Player 1 Hand: "+" ".join(p1_hand_list))
    print("Player 2 Hand: " + " ".join(p2_hand_list))
    # print(card_deck.p1_cards)
    # print(card_deck.p2_cards)
    # card_deck.show_deck()


def play_round(deck_of_cards, number_to_deal):
    p1_point_counter = 0
    p2_point_counter = 0
    # print(deck_of_cards.p1_cards)
    # print(deck_of_cards.p2_cards)
    for x in range(0, number_to_deal):
        print("")
        p1_card = deck_of_cards.p1_cards[x]
        # print(p1_card)
        p2_card = deck_of_cards.p2_cards[x]
        # print(p2_card)
        round_number = x+1
        if compare_cards(p1_card, p2_card, round_number) is True:
            print("Player 1 wins this round!")
            p1_point_counter = p1_point_counter + 1
        else:
            print("Player 2 wins this round!")
            p2_point_counter = p2_point_counter + 1
        # print(p1_point_counter)
        # print(p2_point_counter)
    print("")
    print(Colors.BOLD+"Game over!"+Colors.RESET)
    if p1_point_counter == 1:
        print("Player 1 wins:", p1_point_counter, "round")
    else:
        print("Player 1 wins:", p1_point_counter, "rounds")
    if p2_point_counter == 1:
        print("Player 2 wins:", p2_point_counter, "round")
    else:
        print("Player 2 wins:", p2_point_counter, "rounds")
    if p1_point_counter > p2_point_counter:
        return True
    elif p1_point_counter < p2_point_counter:
        return False
    else:
        return "Tie"


def compare_cards(p1_card, p2_card, round_number):
    ranks_list = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suits_list = ['♣', Colors.RED+'♦'+Colors.RESET, Colors.RED+'♥'+Colors.RESET, '♠']
    print(Colors.BOLD+"Round "+str(round_number)+":"+Colors.RESET)
    print("Player 1:", p1_card['rank'], "of", p1_card['suit'])
    print("Player 2:", p2_card['rank'], "of", p2_card['suit'])
    if p1_card['rank'] == p2_card['rank']:
        # print("a")
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
    deck_of_cards = Deck()
    color = Colors()
    welcome_player()
    create_shuffled_card_deck(deck_of_cards)
    number_to_deal = get_input_on_card_number()
    deal_cards(deck_of_cards, number_to_deal)
    winner = play_round(deck_of_cards, number_to_deal)
    if winner is True:
        print(Colors.GREEN+"Player 1 wins the game!"+Colors.RESET)
    elif winner is False:
        print(Colors.GREEN+"Player 2 wins the game!"+Colors.RESET)
    else:
        print("It's a tie!")
    # print(number_to_deal)


main()






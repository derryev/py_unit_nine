from deck import Deck
from deck import Colors


def welcome_player():
    print("Welcome to the game of compare. You will decide how many cards we get and then we'll play them one by one.")
    print("Whoever has the higher card wins that round. Whoever wins the most rounds wins the game.")


def create_shuffled_card_deck(deck_of_cards):
    deck_of_cards.show_deck()
    deck_of_cards.shuffle_deck()
    deck_of_cards.show_deck()
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

    # print(card_deck.p1_cards)
    # print(card_deck.p2_cards)
    # card_deck.show_deck()


def play_round(deck_of_cards, number_to_deal):
    p1_point_counter = 0
    p2_point_counter = 0
    print(deck_of_cards.p1_cards)
    print(deck_of_cards.p2_cards)
    for x in range(0, number_to_deal):
        p1_card = deck_of_cards.p1_cards[x]
        print(p1_card)
        p2_card = deck_of_cards.p2_cards[x]
        print(p2_card)
        if p1_card['rank'] == p2_card['rank']:
            print("HIIIIII")
        elif p1_card['rank'].isdigit() is True:
            if p2_card['rank'].isdigit is True:
                if int(p1_card['rank']) > p2_card['rank']:
                    p1_point_counter = p1_point_counter+1
                else:
                    p2_point_counter = p2_point_counter + 1
        elif p1_card['rank'].isdigit() is False:
            if p2_card['rank'].isdigit is True:
                # p1 wins bc if their rank is not a number and p2's is, it will automatically be higher than p2's rank
                p1_point_counter = p1_point_counter + 1
        elif p1_card['rank'].isdigit() is True and p2_card['rank'].isdigit is False:
            # p2 wins bc if their rank is not a number and p1's is, it will automatically be higher than p1's rank
            p2_point_counter = p2_point_counter + 1
        elif p1_card['rank'].isdigit() is False and p2_card['rank'].isdigit is False:
            if p1_card['rank'] == 'A':
                p1_point_counter = p1_point_counter + 1
            elif p1_card['rank'] == 'K':
                if p2_card['rank'] == 'A':
                    p2_point_counter = p2_point_counter + 1
                else:
                    p1_point_counter = p1_point_counter + 1
            elif p1_card['rank'] == 'Q':
                if p2_card['rank'] == 'A' or p2_card['rank'] == 'K':
                    p2_point_counter = p2_point_counter + 1
                else:
                    p1_point_counter = p1_point_counter + 1
            elif p1_card['rank'] == 'J':
                p2_point_counter = p2_point_counter + 1
        else:
            print("not working lol")

        print(p1_point_counter)
        print(p2_point_counter)







def main():
    deck_of_cards = Deck()
    welcome_player()
    create_shuffled_card_deck(deck_of_cards)
    number_to_deal = get_input_on_card_number()
    deal_cards(deck_of_cards, number_to_deal)
    play_round(deck_of_cards, number_to_deal)
    # print(number_to_deal)


main()






import random
from replit import clear
from art import logo

def deal_card():
    """Raturns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards."""
    # if 11 in cards and 10 in cards and len(cards) == 2:
    if sum(cards) == 21 and len(cards) == 2:
        return 
    # for card in cards:
    #     if card == 11 and sum(cards) > 21:
    #         cards[card] = 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return f"Your score: {user_score} \nComputer score: {computer_score} \nYou went over. You lose"

    if user_score == computer_score:
        return f"Your score: {user_score} \nComputer score: {computer_score} \nIt is a draw."
    elif computer_score == 0:
        return f"Your score: {user_score} \nComputer score: blackjack \nYou lose."
    elif user_score == 0:
        return f"Your score: blackjack\nComputer score: {computer_score}\nYou win."
    elif user_score > 21:
        return f"Your score: {user_score} \nComputer score: {computer_score} \nYou lose."
    elif computer_score > 21:
        return f"Your score: {user_score} \nComputer score: {computer_score} \nYou win."
    elif user_score < computer_score:
        return f"Your score: {user_score} \nComputer score: {computer_score} \nYou lose."
    elif user_score > computer_score:
        return f"Your score: {user_score} \nComputer score: {computer_score} \nYou win."

def blackjack():
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            another_card = input("Do you want to draw another card? Type 'yes' or 'no'. ")
            if another_card == 'yes':
                user_cards.append(deal_card())
            elif another_card == 'no':
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(compare(user_score, computer_score))

    play_again = input("Do you want to play again? Type 'yes' or 'no'. ")
    if play_again == 'yes':
        clear()
        blackjack()
    else:
        print("Bye bye.")

blackjack()
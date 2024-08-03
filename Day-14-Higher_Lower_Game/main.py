import game_data
import art
import random


def define_option():
    """return a list of detailed person info and discreetly their follower count"""
    random_person = random.choice(game_data.data)
    test = [f"{random_person["name"]}, a {random_person["description"]}, from {random_person["country"]}", random_person["follower_count"]]
    return test


def option_winner(a, b):
    """returns winner based on follower count, returns string A/B"""
    if a[1] > b[1]:
        return "A"
    else:
        return "B"


def game():
    print(art.logo)
    user_guess = 0
    winner = 0
    option_a = define_option()[0]
    game_should_continue = True
    score = 0
    while game_should_continue:
        option_b = define_option()[0]
        if option_a == option_b:
            option_b = define_option()[0]

        winner = option_winner(option_a, option_b)

        print(f"Compare A: {option_a}")
        print(art.vs)
        print(f"Compare B: {option_b}")
        user_guess = input("Who has more followers? Type 'A' or 'B': ")

        if user_guess == winner:
            score += 1
            print(f"Your right! Current score: {score}")
            option_a = option_b
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_should_continue = False


game()


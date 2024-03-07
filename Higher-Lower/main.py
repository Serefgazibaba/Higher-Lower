from data import data
from random import randint
import logo


print(f"{logo.logo}")


def game():
    should_continue = True
    count = 0
    while should_continue:
        first_char_num = randint(0, len(data)-1)
        second_char_num = randint(0, len(data)-1)
        first_char_dic = data[first_char_num]
        second_char_dic = data[second_char_num]
        print(f"Compare A: {first_char_dic['name']},{first_char_dic['description']}, from {first_char_dic['country']}.")
        print(f"{logo.vs}")
        print(f"Against B: {second_char_dic['name']},{second_char_dic['description']}, "
              f"from {second_char_dic['country']}.")
        guess = input("Who has more followers? Type 'A' or 'B' :")
        if guess == "A":
            if first_char_dic['follower_count'] > second_char_dic['follower_count']:
                count += 1
                print(f"You're right! Current score: {count}")
            else:
                print(f"Sorry, that's wrong. Final score: {count}")
                should_continue = False
        else:
            if first_char_dic['follower_count'] < second_char_dic['follower_count']:
                count += 1
                print(f"You're right! Current score: {count}")
            else:
                print(f"Sorry, that's wrong. Final score: {count}")
                should_continue = False


game()

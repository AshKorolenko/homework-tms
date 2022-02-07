character_one = "Villanelle"
character_two = "Ruby Rose"
character_three = "Spongebob Squarepants"
character_four = "Cruella deVil"


while True:
    answer_1 = input("Is your character human? (yes or no): ")

    if answer_1 == "yes":
        answer_2 = input("Is your character an assassin? (yes or no): ")
        if answer_2 == "yes":
            print("Your character is " + character_one)
        elif answer_2 != "yes" and answer_2 != "no":
            print("Invalid input. 'Yes' or 'no' answers only.")
            continue
        else:
            answer_3 = input("Has your character ever played or voiced-over Batwoman? (yes or no): ")
            if answer_3 == "yes":
                print("Your character is " + character_two)
            elif answer_3 != "yes" and answer_2 != "no":
                print("Invalid input. 'Yes' or 'no' answers only.")
                continue
            else:
                answer_4 = input("Is your character a fashion designer? (yes or no): ")
                if answer_4 == "yes":
                    print("Your character is " + character_four)
                elif answer_4 != "yes" and answer_2 != "no":
                    print("Invalid input. 'Yes' or 'no' answers only.")
                    continue

    elif answer_1 == "no":
        print("Your character is " + character_three)

    else:
        print("Invalid input.")

    next_guess = input("Would you like to play again? (yes/no): ")
    if next_guess == "no":
        break

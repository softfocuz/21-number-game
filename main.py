import random

current_number = 0

while True:
    # User turn
    user_count = int(input("How many numbers do you want to say? (1-3): "))

    if user_count not in [1, 2, 3]:
        print("Invalid input!")
        continue

    print("\nYou:")
    for _ in range(user_count):
        current_number += 1
        print(current_number)

        if current_number >= 21:
            print("You said 21. You lose!")
            exit()

    # Computer turn
    computer_count = random.randint(1, 3)

    print(f"\nComputer chooses {computer_count} number(s):")
    for _ in range(computer_count):
        current_number += 1
        print(current_number)

        if current_number >= 21:
            print("Computer said 21. Computer loses!")
            exit()
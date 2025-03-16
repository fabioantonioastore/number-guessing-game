from random import randint


def select_random_number() -> int:
    return randint(1, 100)


if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    print("Select your difficult level:")
    print("1 - Easy (10 chances)")
    print("2 - Medium (5 chances")
    print("3 - Hard (3 chances)")

    level = int(input(""))

    total_chances = None
    match level:
        case 1:
            total_chances = 10
        case 2:
            total_chances = 5
        case 3:
            total_chances = 3
        case _:
            raise f"Invalid level option: {level}"

    print("Let's start the game!")
    number = select_random_number()
    for i in range(total_chances):
        guessing = int(input("Say your guess:\t"))
        if i + 1 == total_chances:
            print(f"You loose, my number was {number}, try again soon!")
            break
        if guessing == number:
            print("You won!")
            break
        if guessing < number:
            print(f"My number is greater than {guessing}")
            print(f"You have more {total_chances - i - 1} chances")
        else:
            print(f"My number is less than {guessing}")
            print(f"You have more {total_chances - i - 1} chances")

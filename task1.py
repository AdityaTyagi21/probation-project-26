import random


def generate_password():
    password = ""

    for i in range(3):
        digit = random.randint(0, 9)
        password += str(digit)

    return password


def get_valid_guess():
    while True:
        guess = input("Enter your 3-digit guess: ").strip()

        if len(guess) == 3 and guess.isdigit():
            return guess

        print("Invalid input! Please enter exactly 3 digits.")


def analyze_guess(password, guess):
    correct_position = []
    wrong_position = []
    not_present = []

    password_digit_count = {}

    for digit in password:
        password_digit_count[digit] = password_digit_count.get(digit, 0) + 1

    remaining_count = password_digit_count.copy()

    # Check correct digit and correct position
    for i in range(3):
        if guess[i] == password[i]:
            correct_position.append(guess[i])
            remaining_count[guess[i]] -= 1

    # Check correct digit in wrong position or digit not present
    for i in range(3):
        if guess[i] == password[i]:
            continue

        digit = guess[i]

        if remaining_count.get(digit, 0) > 0:
            wrong_position.append(digit)
            remaining_count[digit] -= 1
        else:
            not_present.append(digit)

    return correct_position, wrong_position, not_present


def print_hints(correct_position, wrong_position, not_present):
    print("\n--- HINT ---")

    if correct_position:
        print(f" Correct digit & position: {', '.join(correct_position)}")
    else:
        print(" Correct digit & position: None")

    if wrong_position:
        print(f"Correct digit, wrong position: {', '.join(wrong_position)}")
    else:
        print(" Correct digit, wrong position: None")

    if not_present:
        print(f"Not in password: {', '.join(not_present)}")
    else:
        print(" Not in password: None")

    print("------------\n")


def play_game():
    password = generate_password()
    max_attempts = 5
    cnt = 0

    print("PASSWORD CRACKER GAME")
    print(f"Crack the 3-digit password in {max_attempts} attempts.")

    while cnt < max_attempts:
        cnt += 1

        print(f"\nAttempt {cnt}/{max_attempts}")

        guess = get_valid_guess()

        if guess == password:
            print("\nCONGRATULATIONS! ")
            print(f"You cracked the password: {password}")
            print(f"Attempts used: {cnt}")
            return

        correct_position, wrong_position, not_present = analyze_guess(
            password, guess
        )

        print_hints(
            correct_position,
            wrong_position,
            not_present
        )

        remaining_attempts = max_attempts - cnt

        if remaining_attempts > 0:
            print(f"Attempts remaining: {remaining_attempts}")

    print("\n GAME OVER!")
    print(f"The correct password was: {password}")


if __name__ == "__main__":
    play_game()
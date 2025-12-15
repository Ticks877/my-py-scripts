import secrets
import string
import time

def generate_password(length=16):
    characters = (
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits
    )

    while True:
        password = ''.join(secrets.choice(characters) for _ in range(length))

        # Ensure password has all required types
        if (any(c.islower() for c in password) and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password)):
            return password


if __name__ == "__main__":
    try:
        length = int(input("Enter password length (min 8): "))
        if length < 8:
            print("Length too short, using 16 instead.")
            length = 16
    except ValueError:
        print("Invalid input, using default length 16.")
        length = 16

    pwd = generate_password(length)

    print("\nGenerated Password:")
    print(pwd)

    print("\nClosing in 9 seconds...")
    time.sleep(9)

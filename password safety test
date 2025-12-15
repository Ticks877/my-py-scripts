import re
import time

def password_strength(password: str):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long")

    if len(password) >= 12:
        score += 1

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter")

    # Number
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number")

    # Symbol
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character")

    # Rating
    if score <= 2:
        rating = "Very Weak"
    elif score <= 4:
        rating = "Weak"
    elif score <= 6:
        rating = "Good"
    else:
        rating = "Strong"

    return score, rating, feedback


if __name__ == "__main__":
    pwd = input("Enter a password to test: ")
    score, rating, feedback = password_strength(pwd)

    print("\nPassword Strength Result")
    print("-" * 25)
    print(f"Score: {score}/7")
    print(f"Rating: {rating}")

    # SAFE or NOT SAFE
    if rating in ["Good", "Strong"]:
        print("\n✅ Password SAFE")
    else:
        print("\n❌ Password NOT SAFE")

    if feedback:
        print("\nSuggestions:")
        for f in feedback:
            print("-", f)

    print("\nClosing in 5 seconds...")
    time.sleep(5)

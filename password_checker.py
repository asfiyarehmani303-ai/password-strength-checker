import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
        feedback.append("Use at least 12 characters for a stronger password.")
    else:
        feedback.append("Password is too short (minimum 8 characters recommended).")

    # Character variety checks
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Add at least one special character (!@#$%^&* etc.)")

    # Common weak password check
    common_passwords = ["password", "123456", "qwerty", "admin", "letmein", "password123"]
    if password.lower() in common_passwords:
        score = 0
        feedback = ["This is a commonly used password and is very unsafe."]

    # Determine strength label
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, score, feedback


def main():
    print("=== Password Strength Checker ===")
    print("Type 'exit' to quit.\n")

    while True:
        password = input("Enter a password to check: ")
        if password.lower() == "exit":
            print("Goodbye!")
            break

        strength, score, feedback = check_password_strength(password)
        print(f"\nStrength: {strength} (Score: {score}/6)")
        if feedback:
            print("Suggestions to improve:")
            for f in feedback:
                print(f" - {f}")
        print()


if __name__ == "__main__":
    main()
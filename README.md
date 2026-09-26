# Password Strength Checker 🔐

A Python command-line tool that evaluates the strength of a password in real time and gives actionable feedback on how to improve it.

## What It Does

This tool checks a password against several security criteria and assigns a strength score:

- **Length** — rewards passwords 12+ characters, flags anything under 8
- **Character variety** — checks for lowercase, uppercase, numbers, and special characters
- **Common password detection** — flags well-known weak passwords (e.g. "password123", "qwerty")

Based on the total score, the password is rated **Weak**, **Moderate**, or **Strong**, with specific suggestions for improvement.

## How to Run

1. Make sure you have Python 3 installed
2. Clone this repository:
3. https://github.com/asfiyarehmani303-ai/password-strength-checker.git
4. Run the script: python3 password_checker.py
5. Enter any password when prompted. Type `exit` to quit.

## Example 
Enter a password to check: hello123
Strength: Weak (Score: 2/6)
Suggestions to improve:

Use at least 12 characters for a stronger password.
Add uppercase letters.
Add at least one special character (!@#$%^&* etc.)


## Tech Used

- Python 3
- `re` module (regex) for pattern matching

## What I Learned

Building this project helped me understand how real-world password policies are enforced — using regex to detect character types, and combining multiple security checks into a single weighted score rather than a simple pass/fail.

## Future Improvements

- Add a GUI using Tkinter
- Check against a larger breached-password database
- Add entropy-based strength calculation

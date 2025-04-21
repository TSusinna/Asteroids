import os

HIGH_SCORE_FILE = "high_score.txt"

def load_high_score():
    if os.path.exists(HIGH_SCORE_FILE):
        with open(HIGH_SCORE_FILE, "r") as file:
            content = file.read().strip()
            return int(content) if content.isdigit() else 0
    return 0  # Default high score if the file doesn't exist

def save_high_score(high_score):
    with open(HIGH_SCORE_FILE, "w") as file:
        file.write(str(high_score))
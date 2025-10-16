# File: mood_diary.py
# Author: Ardhra
# Project: MyMoodDiary

import datetime
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Colors for pretty output
class color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

# File to store diary entries
DIARY_FILE = "MyMoodDiary.txt"

def write_entry():
    today = datetime.date.today()
    print(f"\n{color.BOLD}Date: {today}{color.ENDC}")

    print("\nHow are you feeling today?")
    print("1. 😊 Happy\n2. 😐 Okay\n3. 😢 Sad\n4. 😡 Angry\n5. ❤️ Loved\n6. 😴 Tired")
    mood_choice = input("Choose your mood (1-6): ")

    moods = {
        "1": "😊 Happy",
        "2": "😐 Okay",
        "3": "😢 Sad",
        "4": "😡 Angry",
        "5": "❤️ Loved",
        "6": "😴 Tired"
    }

    mood = moods.get(mood_choice, "😶 Undefined")

    print("\nWrite about your day below. (Press Enter twice to finish):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    entry_text = "\n".join(lines)

    with open(DIARY_FILE, "a", encoding="utf-8") as f:
        f.write(f"=== {today} ===\nMood: {mood}\n{entry_text}\n\n")

    print(f"\n{color.OKGREEN}✨ Your entry for {today} has been saved! ✨{color.ENDC}")

def view_entries():
    if not os.path.exists(DIARY_FILE):
        print(f"{color.WARNING}No entries found yet. Start writing today!{color.ENDC}")
        return

    print(f"\n{color.HEADER}{color.BOLD}📖 Your Diary Entries 📖{color.ENDC}\n")
    with open(DIARY_FILE, "r", encoding="utf-8") as f:
        print(f.read())

def main():
    while True:
        print(f"""{color.OKCYAN}
═══════════════════════════════════════
        🌸 MyMoodDiary 🌸
═══════════════════════════════════════
1. Write Today’s Entry
2. View Past Entries
3. Exit
═══════════════════════════════════════
{color.ENDC}""")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            write_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            print(f"{color.OKBLUE}Goodbye! Keep journaling 💕{color.ENDC}")
            break
        else:
            print(f"{color.FAIL}Invalid choice. Try again.{color.ENDC}")

if __name__ == "__main__":
    main()


import time

print("=" * 45)
print("       🔋 ESCAPE BATTERY GAME 🔋")
print("=" * 45)

player = input("\nEnter your player name: ")

print("\nWelcome", player, "!")
print("You are trapped inside a secret battery lab.")
print("Solve all 5 levels to escape!")
print("You have 3 attempts for each level.")

levels = [
    {
        "name": "Battery Power",
        "question": "What is 12 + 6?",
        "answer": "18",
        "hint": "Add the two numbers."
    },
    {
        "name": "Secret Number",
        "question": "Find the missing number: 2, 4, 8, 16, ?",
        "answer": "32",
        "hint": "Multiply each number by 2."
    },
    {
        "name": "Battery Terminals",
        "question": "How many terminals does a basic battery have?",
        "answer": "2",
        "hint": "One positive and one negative."
    },
    {
        "name": "Security Code",
        "question": "Solve: 100 - 25 * 2",
        "answer": "50",
        "hint": "Remember multiplication comes first."
    },
    {
        "name": "Final Escape",
        "question": "What device stores electrical energy?",
        "answer": "battery",
        "hint": "It powers your phone and torch."
    }
]

score = 0

for i, level in enumerate(levels, start=1):

    print("\n" + "=" * 45)
    print("LEVEL", i, "-", level["name"])
    print("=" * 45)

    print("\nQuestion:", level["question"])

    attempts = 3

    while attempts > 0:

        answer = input("\nEnter your answer: ").strip().lower()

        if answer == level["answer"]:
            print("\nCorrect answer!")
            print("The door is unlocked!")
            score += 10
            time.sleep(1)
            break

        else:
            attempts -= 1
            print("Wrong answer!")

            if attempts > 0:
                print("Attempts remaining:", attempts)
                print("Hint:", level["hint"])
            else:
                print("You failed this level!")
                print("Correct answer:", level["answer"])

    if attempts == 0:
        print("\nGAME OVER!")
        print("You could not escape the laboratory.")
        break

    if i == 5:
        print("\n" + "*" * 45)
        print("       CONGRATULATIONS!")
        print("       YOU ESCAPED!")
        print("*" * 45)

print("\nPlayer:", player)
print("Your score:", score, "/ 50")

if score == 50:
    print("Amazing! You are a master escape player!")
elif score > 0:
    print("Good job! Keep practicing!")
else:
    print("Better luck next time!")

print("\nThanks for playing ESCAPE BATTERY!")

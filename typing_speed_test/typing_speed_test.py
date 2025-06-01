import time
import random as r


def mistake(partest, usertest):
    """Counts the number of mistakes by comparing the test text and user input."""
    error = 0
    for i in range(min(len(partest), len(usertest))):
        if partest[i] != usertest[i]:
            error += 1
    error += abs(len(partest) - len(usertest))
    return error


def speed_test(start_time, end_time, user_input):
    """Calculates typing speed in Words Per Minute (WPM)."""
    elapsed_time = end_time - start_time
    elapsed_time = max(elapsed_time, 1) 
    words = len(user_input.split())
    speed = (words / elapsed_time) * 60 
    return round(speed, 2), elapsed_time


def calculate_accuracy(partest, usertest):
    """Calculates accuracy percentage."""
    correct_chars = sum(1 for i in range(
        min(len(partest), len(usertest))) if partest[i] == usertest[i])
    total_chars = max(len(partest), len(usertest))
    return round((correct_chars / total_chars) * 100, 2)

test = [
    "The quick brown fox jumps over the lazy dog.",
    "Typing is a skill that improves with practice and patience.",
    "Programming requires logic, problem-solving, and a lot of debugging."
]

test_text = r.choice(test)

print("------------------ TYPING TEST --------------------------\n")
print(test_text)
print("\nStart typing the above text. Press ENTER when done.")

start_time = time.time()
user_input = input("\nType here: ")
end_time = time.time()

wpm, elapsed_time = speed_test(start_time, end_time, user_input)
errors = mistake(test_text, user_input)
accuracy = calculate_accuracy(test_text, user_input)

print("\n------------------ RESULTS --------------------------")
print(f"Typing Speed: {wpm} WPM")
print(f"Time Taken: {round(elapsed_time, 2)} seconds")
print(f"Errors: {errors}")
print(f"Accuracy: {accuracy}%")
print("----------------------------------------------------")

if accuracy > 90:
    print("🔥 Great job! You're a fast and accurate typist!")
elif accuracy > 75:
    print("👍 Good work! Keep practicing to improve your speed and accuracy.")
else:
    print("💡 Keep practicing! You'll get better with time.")

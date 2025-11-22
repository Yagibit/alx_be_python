# daily_reminder.py

# Prompt for user inputs
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process based on priority using match-case
match priority:
    case "high":
        base_message = f"'{task}' is a high priority task"
    case "medium":
        base_message = f"'{task}' is a medium priority task"
    case "low":
        base_message = f"'{task}' is a low priority task"
    case _:
        base_message = f"'{task}' has an unrecognized priority level"

# Handle time-bound or not
if time_bound == "yes":
    final_message = f"Reminder: {base_message} that requires immediate attention today!"
else:
    final_message = f"Note: {base_message}. Consider completing it when you have free time."

# Print final reminder
print(final_message)

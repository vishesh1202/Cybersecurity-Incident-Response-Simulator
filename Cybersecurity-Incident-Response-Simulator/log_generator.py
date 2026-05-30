import random

events = [
    "User Login",
    "Failed Login",
    "Ransomware Detected",
    "Phishing Email Opened",
    "Large Data Transfer"
]

with open("logs/generated_logs.txt", "w") as file:
    for i in range(50):
        file.write(random.choice(events) + "\n")

print("Logs Created!")
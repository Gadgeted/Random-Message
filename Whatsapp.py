import pywhatkit as kit
import random
import schedule
import time
import pyautogui
from datetime import datetime

# List of sweet messages
messages = [
    "Good morning, my love! ❤ Hope you have a beautiful day!",
    "Just thinking about you 😘 Hope your day is as amazing as you are!",
    "You're my sunshine ☀ Have a fantastic day, baby!",
    "I love you so much! 💖 Stay happy and take care!",
    "You make my world brighter 🌍✨ Can't wait to talk to you later!"
]

# (include country code, e.g., +254...)
recipient_number = "+254758018440"

# Function to send a random message and press Enter automatically
def send_message():
    message = random.choice(messages)
    try:
        kit.sendwhatmsg_instantly(recipient_number, message)
        time.sleep(5)  # Wait for WhatsApp Web to load
        pyautogui.press("enter")  # Simulate pressing Enter to send message
        print(f"Sent: '{message}' at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    except Exception as e:
        print(f"Failed to send message: {e}")

# Schedule the message to be sent automatically at a specific time every day
schedule.every().day.at("22:23").do(send_message)  # Adjust time as needed

# Infinite loop to keep the script running
while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute if it's time to send a message

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
    "Every moment with you is a gift. Have an incredible day, my love! 💕"
    "You’re always on my mind, making my heart smile 😊 Wishing you a wonderful day!"
    "I can’t wait to see your smile today 😄 You make everything better!"
    "You’re the reason my heart feels so full. Have an amazing day, beautiful! 💖"
    "Just wanted to remind you how much you mean to me 💌 I’m thinking of you always."
    "My day instantly gets better just by thinking of you 😘 Have a great day, love!"
    "You light up my life in ways I can't describe. Hope your day shines just as bright! 🌟"
]

# (include country code, e.g., +254...)
recipient_number = "+254797341497"

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
schedule.every().day.at("22:05").do(send_message)  # Adjust time as needed

# Infinite loop to keep the script running
while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute if it's time to send a message

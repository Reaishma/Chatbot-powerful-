import random
import datetime
import pytz
import getpass
import hashlib

# User database
users = {}

def register_user():
    username = input("Enter a username: ")
    password = getpass.getpass("Enter a password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    users[username] = hashed_password
    print("User registered successfully!")

def login_user():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in users and users[username] == hashed_password:
        print("Login successful!")
        return username
    else:
        print("Invalid username or password.")
        return None

def get_current_time():
    timezone = pytz.timezone('Asia/Kolkata')
    current_time = datetime.datetime.now(timezone)
    return current_time.strftime("%H:%M:%S")

def get_current_date():
    timezone = pytz.timezone('Asia/Kolkata')
    current_date = datetime.datetime.now(timezone)
    return current_date.strftime("%Y-%m-%d")

def convert_length():
    print("Conversion options:")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    choice = input("Enter your choice: ")
    if choice == "1":
        km = float(input("Enter distance in kilometers: "))
        miles = km * 0.621371
        print(f"{km} kilometers is equal to {miles} miles.")
    elif choice == "2":
        miles = float(input("Enter distance in miles: "))
        km = miles * 1.60934
        print(f"{miles} miles is equal to {km} kilometers.")

def convert_weight():
    print("Conversion options:")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    choice = input("Enter your choice: ")
    if choice == "1":
        kg = float(input("Enter weight in kilograms: "))
        pounds = kg * 2.20462
        print(f"{kg} kilograms is equal to {pounds} pounds.")
    elif choice == "2":
        pounds = float(input("Enter weight in pounds: "))
        kg = pounds * 0.453592
        print(f"{pounds} pounds is equal to {kg} kilograms.")

intents = {
    "greeting": ["hello", "hi", "hey"],
    "goodbye": ["goodbye", "bye", "see you later"],
    "thanks": ["thanks", "thank you"],
    "help": ["help", "what can you do"],
    "weather": ["weather", "forecast"],
    "time": ["time", "current time"],
    "date": ["date", "today's date"],
    "length": ["length", "distance"],
    "weight": ["weight", "mass"],
}

responses = {
    "greeting": ["Hello!", "Hi!", "Hey!"],
    "goodbye": ["Goodbye!", "See you later!", "Bye!"],
    "thanks": ["You're welcome!", "No problem!", "Thank you!"],
    "help": ["How can I assist you?", "What do you need help with?", "I'm here to help!"],
    "weather": ["The weather is sunny today!", "It's cloudy outside.", "I don't have real-time weather updates, but you can check your local forecast."],
}

def get_response(user_input):
    user_input = user_input.lower()
    for intent, keywords in intents.items():
        for keyword in keywords:
            if keyword in user_input:
                if intent == "time":
                    return "The current time is " + get_current_time()
                elif intent == "date":
                    return "Today's date is " + get_current_date()
                elif intent == "length":
                    convert_length()
                    return ""
                elif intent == "weight":
                    convert_weight()
                    return ""
                else:
                    return random.choice(responses[intent])
    return "I didn't understand that. Can you please rephrase?"

def main():
    print("Welcome to Powerful Chatbot!")
    print("1. Register")
    print("2. Login")
    choice = input("Enter your choice: ")
    username = None
    if choice == "1":
        register_user()
        username = login_user()
    elif choice == "2":
        username = login_user()
    if username:
        print("Type 'quit' to exit.")
        while True:
            user_input = input("User: ")
            if user_input.lower() == "quit":
                break
            response = get_response(user_input)
            if response:
                print("Powerful: ", response)

if __name__ == "__main__":
    main()
import random

# Predefined list of quotes
quotes = [
    "The best way to get started is to quit talking and begin doing. - Walt Disney",
    "The pessimist sees difficulty in every opportunity. The optimist sees opportunity in every difficulty. - Winston Churchill",
    "Don’t let yesterday take up too much of today. - Will Rogers",
    "You learn more from failure than from success. Don’t let it stop you. Failure builds character. - Unknown",
    "It’s not whether you get knocked down, it’s whether you get up. - Vince Lombardi"
]

def show_menu():
    print("\nRandom Quote Generator")
    print("1. Get a Random Quote")
    print("2. Add a New Quote")
    print("3. View All Quotes")
    print("4. Exit")

def get_random_quote():
    print("\nHere’s a random quote for you:")
    print(random.choice(quotes))

def add_new_quote():
    new_quote = input("\nEnter a new quote: ")
    quotes.append(new_quote)
    print("Quote added successfully!")

def view_all_quotes():
    print("\nAll Quotes:")
    for i, quote in enumerate(quotes, start=1):
        print(f"{i}. {quote}")

# Main program loop
while True:
    show_menu()
    choice = input("\nChoose an option (1-4): ")
    
    if choice == "1":
        get_random_quote()
    elif choice == "2":
        add_new_quote()
    elif choice == "3":
        view_all_quotes()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

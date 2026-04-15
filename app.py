import webbrowser

print("🤖 Hello! I am AI Bot.")
name = input("What's your name? : ").strip()

print(f"Nice to meet you, {name}! 😊")

# Predefined popular websites
sites = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "wikipedia": "https://www.wikipedia.org",
    "instagram": "https://www.instagram.com",
    "facebook": "https://www.facebook.com",
    "twitter": "https://www.twitter.com",
    "chatgpt": "https://chat.openai.com"
}

while True:
    print("\nWhat do you want to do?")
    print("1. Open a website")
    print("2. Search something on Google")
    print("Type 'exit' to quit")

    choice = input("Enter your choice: ").strip().lower()

    if choice == "exit":
        print(f"Goodbye {name}! 👋")
        break

    elif choice == "1":
        site_name = input("Enter website name (e.g., google, youtube): ").strip().lower()

        if site_name in sites:
            url = sites[site_name]
        else:
            url = f"https://www.{site_name}.com"

        print(f"Opening {url} 🚀")
        webbrowser.open(url)

    elif choice == "2":
        query = input("What do you want to search? : ").strip()
        search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
        
        print(f"Searching for '{query}' 🔍")
        webbrowser.open(search_url)

    else:
        print("❌ Invalid choice. Please try again.")

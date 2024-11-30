import string
import secrets

# in-memory database to store URL mappings
url_mapping = {}

# generate a random short code, the real magic.
def generate_short_code():
    return ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(6))

# shorten a URL
def shorten_url(original_url):
    """
    Shortens the given URL and stores it in the in-memory database.
    Returns the short code.
    """
    short_code = generate_short_code()
    while short_code in url_mapping:  # to make sure they are all different, yeah?
        short_code = generate_short_code()
    
    url_mapping[short_code] = original_url
    return short_code

# retrieve the original URL
def get_original_url(short_code):
    """
    Retrieves the original URL from the short code.
    Returns None if the short code does not exist.
    """
    return url_mapping.get(short_code)

# main function for users, made by Cpl Yeh
def main():
    print("Welcome to the URL Shortener!")
    while True:
        print("\nChoose an option:")
        print("1. Shorten a URL")
        print("2. Retrieve original URL")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ").strip()
        
        if choice == '1':
            original_url = input("Enter the URL to shorten: ").strip()
            short_code = shorten_url(original_url)
            print(f"Shortened URL: http://localhost/{short_code}")
        elif choice == '2':
            short_code = input("Enter the short code: ").strip()
            original_url = get_original_url(short_code)
            if original_url:
                print(f"Original URL: {original_url}")
            else:
                print("Error: Short code not found.")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

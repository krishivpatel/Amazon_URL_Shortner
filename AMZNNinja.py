import re
import os
import pyperclip
from termcolor import colored
import colorama

colorama.init()

# Banner text
BANNER = colored('''
 _    _ ____  ____  ___  _   _   _____ _______   _______ _____ ____  
| |  | |  _ \|  _ \|_ _|| \ | | |_   _|_   _\ \ / /_   _| ____|  _ \ 
| |  | | |_) | |_) || | |  \| |   | |   | |  \ V /  | | |  _| | |_) |
| |__| |  _ <|  _ < | | | |\  |   | |   | |   | |   | | | |___|  _ < 
 \____/|_| \_\_| \_\___||_| \_|   |_|   |_|   |_|   |_| |_____|_| \_\

''', 'cyan')

def clear_screen():
    """Clear the console window"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """Print the program banner"""
    clear_screen()
    print(BANNER)
    print(colored('-' * 60, 'green'))

def shorten_url():
    # Ask user for URL to shorten
    url = input('\nPlease enter an Amazon product URL to shorten: ')

    # Validate URL
    while not re.match(r'^(http(s)?://)?(www\.)?amazon\.(com|co\.uk|ca|in|com\.au|com\.mx|com\.br|ae|com\.tr|sg|nl|se|fr|de|it|es)/.*(/dp/[\w-]+|/gp/product/[\w-]+).*$', url):
        url = input('Invalid URL. Please enter a valid Amazon product URL: ')

    # Extract domain and slug from URL
    domain, slug = re.findall(r'^(https?://)?(www\.)?amazon\.(com|co\.uk|ca|in|com\.au|com\.mx|com\.br|ae|com\.tr|sg|nl|se|fr|de|it|es)/.*(/dp/[\w-]+|/gp/product/[\w-]+).*$', url)[0][2:]

    # Construct shortened URL
    shortened_url = f'https://amzon.{domain}{slug}'

    # Copy to clipboard
    pyperclip.copy(shortened_url)

    return shortened_url


def main():
    """Main program function"""
    while True:
        print_banner()
        print(colored('Welcome to Amazon URL Shortener!', 'blue'))
        print(colored('-' * 60, 'green'))
        
        # Shorten URL
        shortened_url = shorten_url()
        
        if shortened_url is not None:
            # Display shortened URL and copy to clipboard
            print(colored('Here is your shortened URL:', 'green'))
            print(colored(shortened_url, 'cyan'))
            pyperclip.copy(shortened_url)

        # Prompt user for another URL or exit
        while True:
            print(colored('-' * 60, 'green'))
            choice = input(colored('Do you want to shorten another URL? (y/n): ', 'blue')).lower()
            if choice == 'y':
                break
            elif choice == 'n':
                print(colored('Thanks for using Amazon URL Shortener!', 'blue'))
                return
            else:
                print(colored('Invalid choice. Please enter "y" or "n"', 'red'))

if __name__ == '__main__':
    main()

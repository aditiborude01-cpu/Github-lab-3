import os
import sys
import time
import requests
from colorama import Fore, Style, init

# Terminal colors initialize karein
init(autoreset=True)

def clear_terminal():
    """Terminal screen ko clean karne ke liye"""
    os.system('cls' if os.name == 'nt' else 'clear')

def fetch_github_user(username):
    """GitHub API se user ka data fetch karne ke liye function"""
    url = f"https://github.com{username}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            print(Fore.RED + f"\n[Error] Username '{username}' nahi mila. Kripya sahi naam dalein.")
            return None
        else:
            print(Fore.RED + f"\n[Error] API Request fail ho gayi. Status Code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"\n[Error] Connection Issue: {e}")
        return None

def main():
    clear_terminal()
    print(Fore.CYAN + Style.BRIGHT + "=" * 45)
    print(Fore.CYAN + Style.BRIGHT + "       WELCOME TO GITHUB PROFILE TRACKER     ")
    print(Fore.CYAN + Style.BRIGHT + "=" * 45)
    
    # User se username input lein
    username = input(Fore.YELLOW + "Enter GitHub Username to track: ").strip()
    if not username:
        print(Fore.RED + "Username khali nahi ho sakta. Script band ho rahi hai.")
        return

    clear_terminal()
    print(Fore.GREEN + f"Fetching data for '{username}'... Please wait.\n")
    time.sleep(1)

    user_data = fetch_github_user(username)
    
    if user_data:
        clear_terminal()
        print(Fore.GREEN + Style.BRIGHT + "============== USER PROFILE ==============")
        print(Fore.BLUE + f" Name        : {user_data.get('name', 'N/A')}")
        print(Fore.BLUE + f" Bio         : {user_data.get('bio', 'No bio available')}")
        print(Fore.BLUE + f" Location    : {user_data.get('location', 'Not specified')}")
        print("-" * 42)
        print(Fore.MAGENTA + f" Public Repos: {user_data.get('public_repos', 0)}")
        print(Fore.MAGENTA + f" Followers   : {user_data.get('followers', 0)}")
        print(Fore.MAGENTA + f" Following   : {user_data.get('following', 0)}")
        print(Fore.GREEN + Style.BRIGHT + "==========================================")
        print(Fore.YELLOW + f"\nProfile Link: {user_data.get('html_url')}\n")
    else:
        print(Fore.YELLOW + "\nKoi data fetch nahi kiya ja saka. Dobara koshish karein.\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\nTracker closed by user. Bye!")

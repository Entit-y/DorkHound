import sys
import os
import json
import time
from googlesearch import search
from colorama import Fore, Style

# Define the banner
BANNER = """
\033[31m
██████╗  ██████╗ ██████╗ ██╗  ██╗     ██╗  ██╗ ██████╗ ██╗   ██╗███╗   ██╗██████╗ 
██╔══██╗██╔═══██╗██╔══██╗██║ ██╔╝     ██║  ██║██╔═══██╗██║   ██║████╗  ██║██╔══██╗
██║  ██║██║   ██║██████╔╝█████╔╝█████╗███████║██║   ██║██║   ██║██╔██╗ ██║██║  ██║
██║  ██║██║   ██║██╔══██╗██╔═██╗╚════╝██╔══██║██║   ██║██║   ██║██║╚██╗██║██║  ██║
██████╔╝╚██████╔╝██║  ██║██║  ██╗     ██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║██████╔╝
╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═════╝ 
\033[0m                                                                                
"""

# Load existing dorks from dork-list.json
with open("dork-list.json", "r") as f:
    dorks = json.load(f)

# Check if website argument is provided
if len(sys.argv) != 2:
    print(Fore.RED + "Usage: python DorkHound.py <website>")
    sys.exit(1)

website = sys.argv[1]
print(BANNER)  # Display the banner
print(Fore.MAGENTA + f"Target website: {Fore.RED}{website}")

DORK_LIST_FILE = "dork-list.json"
RESULTS_FILE = "dork_results.md"

def read_dork_list(file_path):
    try:
        with open(file_path, "r") as f:
            dorks = json.load(f)
    except FileNotFoundError:
        print(Fore.RED + f"Error: File {file_path} not found.")
        return None
    return dorks

def google_dorking(website, dorks):
    results = {}
    print(Fore.MAGENTA + "Starting Google dorking...")
    for category, dork_dict in dorks.items():
        print(Fore.YELLOW + f"Category: {category}")
        for dork, description in dork_dict.items():
            print(Fore.MAGENTA + f"Searching for: {dork} - {Fore.RED}{description}")
            query = f"site:{website} {dork}"
            try:
                results[dork] = list(search(query, stop=10))
                print(Fore.GREEN + f"Found {len(results[dork])} results.")
                time.sleep(5)  # Introduce a delay of 5 seconds between requests
            except Exception as e:
                if "HTTP Error 429" in str(e):
                    print("Too Many Requests. Pausing for 120 seconds...")
                    print("Google is blocking our requests...")
                    print("Scan will wait for at least 6 minutes before resuming...")
                    time.sleep(360)
                elif "WinError 10060" in str(e):
                    print("No Response From Google's Server...")
                    print("Pausing for 20 seconds...")
                    time.sleep(20)
                    print("Resuming...")
                else:
                    print(f"An error occurred with dork '{dork}': {e}")
    print(Fore.GREEN + "Google dorking completed.")
    return results

def save_results_to_md(results, dorks):
    print(Fore.GREEN + f"Saving results to {Fore.RED}Markdown file...")
    with open(RESULTS_FILE, "w") as f:
        for category, dork_dict in dorks.items():
            f.write(f"## {category}\n\n")
            for dork, urls in results.items():
                if dork in dork_dict:
                    f.write(f"### {dork} - {dork_dict[dork]}\n\n")
                    for url in urls:
                        f.write(f"- [{url}]({url})\n")
                    f.write("\n")
    print(Fore.GREEN + f"Results saved to {RESULTS_FILE}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Fore.RED + "Usage: python google_dork.py <website>")
        sys.exit(1)

    website = sys.argv[1]
    print(Fore.MAGENTA + f"Target website: {Fore.RED}{website}")

    print(Fore.MAGENTA + "Reading dork list...")
    dorks = read_dork_list(DORK_LIST_FILE)
    if not dorks:
        sys.exit(1)
    
    print(Fore.MAGENTA + "Starting Google dorking process...")
    results = google_dorking(website, dorks)
    save_results_to_md(results, dorks)  # Pass the 'dorks' dictionary as well




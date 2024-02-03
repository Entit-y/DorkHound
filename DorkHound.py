import sys
import os
import json
import time
from googlesearch import search

DORK_LIST_FILE = "dork-list.json"
RESULTS_FILE = "dork_results.md"

def read_dork_list(file_path):
    try:
        with open(file_path, "r") as f:
            dorks = json.load(f)
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return None
    return dorks

def google_dorking(website, dorks):
    results = {}
    print("Starting Google dorking...")
    for category, dork_dict in dorks.items():
        print(f"Category: {category}")
        for dork, description in dork_dict.items():
            print(f"Searching for: {dork} - {description}")
            query = f"site:{website} {dork}"
            try:
                results[dork] = list(search(query, stop=5))
                print(f"Found {len(results[dork])} results.")
                time.sleep(2)  # Introduce a delay of 2 seconds between requests
            except Exception as e:
                print(f"An error occurred with dork '{dork}': {e}")
        time.sleep(10)  # Introduce a delay between batches of dorks
    print("Google dorking completed.")
    return results

def save_results_to_md(results, dorks):
    print("Saving results to Markdown file...")
    with open(RESULTS_FILE, "w") as f:
        for category, dork_dict in dorks.items():
            f.write(f"## {category}\n\n")
            for dork, urls in results.items():
                if dork in dork_dict:
                    f.write(f"### {dork} - {dork_dict[dork]}\n\n")
                    for url in urls:
                        f.write(f"- [{url}]({url})\n")
                    f.write("\n")
    print(f"Results saved to {RESULTS_FILE}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python google_dork.py <website>")
        sys.exit(1)

    website = sys.argv[1]
    print(f"Target website: {website}")

    print("Reading dork list...")
    dorks = read_dork_list(DORK_LIST_FILE)
    if not dorks:
        sys.exit(1)
    
    print("Starting Google dorking process...")
    results = google_dorking(website, dorks)
    save_results_to_md(results, dorks)  # Pass the 'dorks' dictionary as well




import json

# Load existing dorks from dork-list.json
with open("dork-list.json", "r") as f:
    dorks = json.load(f)

# Prompt user for custom dork and description
custom_dork = input("Enter the custom dork you want to add: ")
description = input("Enter a description for the custom dork: ")

# Prompt user to select or input a category
print("Select a category or input a custom category:")
categories = list(dorks.keys())
for i, category in enumerate(categories, 1):
    print(f"{i}. {category}")
print(f"{len(categories) + 1}. Add Custom Category")
choice = int(input("Enter your choice: "))

if choice == len(categories) + 1:
    custom_category = input("Enter the name of the custom category: ")
    dorks[custom_category] = {custom_dork: description}
else:
    selected_category = categories[choice - 1]
    dorks[selected_category][custom_dork] = description

# Write updated dorks to dork-list.json
with open("dork-list.json", "w") as f:
    json.dump(dorks, f, indent=4)

print("Custom dork added successfully.")

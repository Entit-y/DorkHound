# DorkHound
DorkHound is a Python script designed to facilitate Google dorking—a technique used by security professionals and enthusiasts to discover sensitive information exposed on websites. By leveraging predefined search queries (dorks), DorkHound helps users uncover potential vulnerabilities, configuration issues, and other valuable insights within target domains. With DorkHound, users can automate the process of reconnaissance and information gathering, enabling them to enhance their security assessments and investigations efficiently.

![DorkHound](<DorkHound Banner.png>)

## Installation:
1. Clone this repo:
```bash
https://github.com/Entit-y/DorkHound
```
2. Change your directory into the cloned repo
```bash
cd DorkHound
```

## Usage:
2. Run this command in your terminal(replace target.com to the domain of your target):
```bash
python3 DorkHound.py target.com
```
The output is automatically saved to "dork_results.md"
I recommend the [Obsidian](https://obsidian.md/download) note taking app for viewing the results

## Adder.py
This script can be used to ad custom dorks to be used by the main script(DorkHound.py)

## Usage:
```bash
python adder.py
```
Follow the prompts to input a custom dork and select a category from the existing categories or input a custom category.

Input a custom dork when prompted.
Choose a category or input a custom category when prompted.
The custom dork will be added to the dork-list.json file for use by the DorkHound.py script

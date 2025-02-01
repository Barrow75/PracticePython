# Prompt: Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file,
# and print out the results to the screen
from doctest import Example
from itertools import count

import requests
from bs4 import BeautifulSoup

base_url = 'https://www.practicepython.org/assets/nameslist.txt'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")


with open("ExampleFile.txt", "w", encoding="utf-8") as f:
        f.write(r.text.strip())

with open("ExampleFile.txt", 'r') as f:
    lines = f.readlines()
    total_count = 0
    total_count2 = 0
    total_count3 = 0
    for line in lines:
        if "Darth" in line:
            count = line.count("Darth")
            total_count += count
        elif "Luke" in line:
            count2 = line.count("Luke")
            total_count2 += count2
        else:
            count3 = line.count("Lea")
            total_count3 += count3
    print(f"Total Darth in file is {total_count}, Luke is {total_count2}, and Lea is {total_count3}")













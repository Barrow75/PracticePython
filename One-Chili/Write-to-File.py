# Prompt: Take the code from the How To Decode A Website exercise
# (if you didn’t do it or just want to play with some different code,
# use the code from the solution), and instead of printing the results to a screen, write the results to a txt file.


import requests
from bs4 import BeautifulSoup

base_url = 'https://en.wikipedia.org/wiki/Binary_search'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")


with open("ExampleFile.txt", "w", encoding="utf-8") as f:
    for paragraph in soup.find_all("p"):
        f.write(paragraph.text.strip() + "\n\n")


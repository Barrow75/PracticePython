# Prompt: Given two .txt files that have lists of numbers in them, find the numbers that are overlapping.
# One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.



import requests


#online_file = '[Enter link of text file from online]'

#request = requests.get(online_file)


with open('Prime_Numbers.txt', 'r') as pf, open('Happy_Numbers.txt', 'r') as hf:
    prime = set(int(line.strip()) for line in pf.readlines())
    happy = set(int(line.strip()) for line in hf.readlines())

    similar_numbers = sorted(prime.intersection(happy))




with open('Similar_numbers.txt', 'w') as file:
    for number in similar_numbers:
        file.write(str(number) + '\n')

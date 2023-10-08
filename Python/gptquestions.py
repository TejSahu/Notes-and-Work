# To generate random password of length 8

"""import random
import string

def generate_password():
    password = ''
    characters = string.ascii_letters + string.digits
    for i in range(8):
        password += random.choice(characters)
    return password

print(generate_password())"""

# All the links in the URL

"""import requests
from bs4 import BeautifulSoup

def extract_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup)
    links = []
    for link in soup.find_all('a'):
        print(link)
        links.append(link.get('href'))
    return links

print(extract_links("https://www.httpbin.org"))"""

# Return word count in each sentence
"""poem = "Earlier today, former MP Atiq Ahmed along with his brother were produced before a court in Prayagraj amid " \
      "high-security deployment. While Atiq Ahmed was brought to Prayagraj via road from Sabarmati Jail in Gujarat" \
      " for his production, his brother Khalid Azim alias Ashraf was brought from a Bareilly jail."""
"""def count_words_in_sentences(text):
    sentences = text.split('. ')
    word_counts = []
    for sentence in sentences:
        words = sentence.split()
        word_counts.append(len(words))
    return word_counts

print(count_words_in_sentences(poem))"""


def sort_log_file(log_file, sort_column):
    # Read the log file into a list of lines
    with open(log_file, 'r') as f:
        lines = f.readlines()

    # Split each line into columns and convert the sort column to a numeric value
    data = []
    for line in lines:
        columns = line.strip().split(' ')
        sort_value = int(columns[sort_column])
        data.append((sort_value, line))

    # Sort the data by the sort column
    data.sort()

    # Write the sorted data back to the log file
    with open(log_file, 'w') as f:
        for _, line in data:
            f.write(line)

sort_log_file("Linux.log", 1)

with open("Linux.log", 'r') as log:
    print(log.readlines())

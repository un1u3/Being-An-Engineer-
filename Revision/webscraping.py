from bs4 import BeautifulSoup
import requests

# Open and parse the HTML file
with open('simple.html') as html_file:  # Corrected typo here
    soup = BeautifulSoup(html_file, 'lxml')

# Print the parsed content
print(soup)

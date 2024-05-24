import requests
from bs4 import BeautifulSoup

url = 'https://www.sab.ac.lk/'

# Send a GET request to the URL
res = requests.get(url)

# htmlcontent = res.content
# print(htmlcontent)

# Parse the content of the page with BeautifulSoup
soup = BeautifulSoup(res.content, 'html.parser')

# extract main title
title = soup.title
print(title.string)
print("\n")


# extract heading 2 titles
titles = soup.find_all('h2', class_='title')
for title in titles:
    print(title.get_text())

print("\n<p> elements:\n")

# extract p tag
elements = soup.find_all('p')
for element in elements:
    print(element)

print("\n All Links::\n")

# get all links
anchor = soup.find_all('a')
for i in anchor:
    print(i.get('href'))


# extact all text
# print(soup.get_text())



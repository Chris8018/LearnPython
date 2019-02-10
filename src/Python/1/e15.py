# import requests
# from bs4 import BeautifulSoup
#
# base_url = 'http://www.nytimes.com'
# r = requests.get(base_url)
# soup = BeautifulSoup(r.text, "lxml")
#
# for story_heading in soup.find_all(class_="balanceHeadlines"):
#     if story_heading.a:
#         print(story_heading.a.text.replace("\n", " ").strip())
#     else:
#         print(story_heading.contents[0].strip())


# **Online Solution**

import requests
from bs4 import BeautifulSoup

url = 'http://www.nytimes.com/'
ttl_lst = []

# request URL
r = requests.get(url)

# Parsing
soup = BeautifulSoup(r.text, "lxml")

#                    tag          {attributes}
title = soup.findAll('h2', {'class': 'css-bzeb53 esl82me2'})
for row in title:
    ttl_lst.append(row.text)

print(ttl_lst)

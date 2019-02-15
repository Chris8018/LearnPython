import requests
from bs4 import BeautifulSoup

urls = ['https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
        , 'http://content.time.com/time/magazine/article/0,9171,2005869,00.html'
        , 'https://www.theregister.co.uk/2014/08/26/top_ten_gaming_keyboard_and_mouse_combos/'
        ]
url = urls[0]

# Request URL
soup = BeautifulSoup(requests.get(url).text, "lxml")


for line in soup.find_all('p'):
    print(line.getText())

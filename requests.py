import bs4
import requests

text = str("Tim Berners-Lee")
url = str('https://google.com/search?q=' + text)

request_result = requests.get(url)

soup = bs4.BeautifulSoup(request_result.text,"html.parser")
for link in soup.find_all('a'):
    print(link.get('href'))
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta2
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')


#body-content > div.newest-list > div > table > tbody > tr:nth-child(1)
#body-content > div.newest-list > div > table > tbody > tr:nth-child(2)
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
#body-content > div.newest-list > div > table > tbody > tr:nth-child(2) > td.number
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis
trs = soup.select("#body-content > div.newest-list > div > table > tbody > tr")

print(trs)

for tr in trs:
    rank_dummy = tr.select_one("td.number")
    for tag in rank_dummy.find_all("span", {"class": "rank"}):
        tag.replaceWith("")
    rank = rank_dummy.text.strip()
    info = tr.select_one("td.info")
    title = info.select_one("a.title.ellipsis").text.strip()
    artist = info.select_one("a.artist.ellipsis").text.strip()
    print(rank, title, artist)
    doc = {
        "rank":rank,
        "title":title,
        "artist":artist
    }
    db.songs.insert_one(doc)
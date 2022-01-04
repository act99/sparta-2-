import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta2

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 코딩 시작
#old_content > table > tbody > tr:nth-child(2) >
#old_content > table > tbody > tr:nth-child(3) > td:nth-child(1) > img
#old_content > table > tbody > tr:nth-child(8) > td:nth-child(1) > img
#old_content > table > tbody > tr:nth-child(3) > td.point
trs = soup.select("#old_content > table > tbody > tr")

# for tr in trs:
#     a_tag = tr.select_one(" td.title > div > a")
#     if a_tag is not None:
#         title = a_tag.text
#         rank_tag = tr.select_one("td")
#         rank = rank_tag.select_one("img")["alt"]
#         point = tr.select_one("td.point").text
#         print(rank, title, point)
#
#         doc = {'rank':rank,'title':title,'point':point}
#         db.movies.insert_one(doc)

mx_point = db.movies.find_one({"title":"매트릭스"}, {"_id":False})["point"]
mx_same = list(db.movies.find({"point":mx_point},{"_id":False}))
# for same in mx_same:
#     print(same)

mx_make0 = db.movies.update_one({"title":"매트릭스"},{'$set':{'point':'0'}})
print(mx_point)
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.

movie = db.movies.find_one({'title': '월-E'})
target_star = movie["star"]

db.movies.update_many({"star":target_star}, {'$set': {'star':'0'}})

for same_movie in list(db.movies.find({'star': target_star})):
    
    print(same_movie['title'],same_movie['star'])



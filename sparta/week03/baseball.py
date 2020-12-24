import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://sports.news.naver.com/kbaseball/record/index.nhn?category=kbo',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')
# regularTeamRecordList_table > tr:nth-child(1) > td.tm > div > img
# team_NC
#regularTeamRecordList_table > tr:nth-child(1) > th > strong
teams = soup.select('#regularTeamRecordList_table > tr')
for kborank in teams:
    team_name = kborank.select_one('td > div > span')
    if team_name is not None:
        rank = kborank.select_one('th > strong')

        print(rank.text,team_name.text)

#############################
# (입맛에 맞게 코딩)
#############################
#regularTeamRecordList_table > tr:nth-child(1) > th > strong
#team_NC
#team_OB


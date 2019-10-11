import urllib.parse, requests, pprint, json
from datetime import date

today = date.today().strftime('%Y%m%d')
time  = input(date.today().strftime('%Y년 %m월 %d일')+'검색하고싶은 시간을 입력하세요(예.0230) :')

url    = 'http://newsky2.kma.go.kr/service/SecondSrtpdFrcstInfoService2/ForecastSpaceData'
params = 'ServiceKey=7deEpltz9ms6YRj%2BcoFs4q8jk1igEb9FFJVlb8bj%2F%2FyW4qJscGYZCmZ041noTjEKF4T' \
         '127&_type=json'

response = requests.get(url + "?" +params)
response.raise_for_status()

SKY = {'1':'맑음','3':'구름많음','4':'흐림'}

weatherData = json.loads(response.text)
#print(weatherData)

if weatherData['response']['body']['items']:
    for x in weatherData['response']['body']['items']['item']:
        if x['category'] == 'SKY':
            print('하늘 상태는 ' + SKY[str(x['fcstValue'])] + " 입니다.")
else:
    print(date.today().strftime('%Y년 %m월 %d일')+'')


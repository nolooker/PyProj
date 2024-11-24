import sys
import io

# 출력 스트림의 기본 인코딩 설정
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

import requests

# API 키와 엔드포인트 설정
api_key = 'St24iaoXT67tzOIgB5sB4bEYWGxyrVly'

url = f'https://api.nytimes.com/svc/mostpopular/v2/viewed/1.json?api-key={api_key}'

# API 요청
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    for article in data['results']:
        print(f"Title: {article['title']}")
        print(f"URL: {article['url']}\n")
        
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")

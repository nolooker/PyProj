import sys
import io

# 출력 스트림의 기본 인코딩 설정
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

import requests
from deep_translator import GoogleTranslator


# API 키와 엔드포인트 설정
api_key = 'St24iaoXT67tzOIgB5sB4bEYWGxyrVly'

url = f'https://api.nytimes.com/svc/mostpopular/v2/viewed/1.json?api-key={api_key}'

# API 요청
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    for article in data['results']:
        original_title = article['title']  # 원본 제목
        
        # 번역 수행
        translated_title = GoogleTranslator(source='en', target='ko').translate(original_title)
        print(f"Original Title: {original_title}")
        print(f"Translated Title: {translated_title}")
        print(f"URL: {article['url']}\n")
        
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
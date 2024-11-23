# -*- coding: utf-8 -*-
import sys
from pytrends.request import TrendReq
import time

# UTF-8 인코딩 출력
sys.stdout.reconfigure(encoding='utf-8')

# PyTrends 설정
pytrends = TrendReq(hl='ko', tz=360)

# 키워드 리스트
keywords = ['파이썬', 'RPA', '머신 러닝']

for keyword in keywords:
    try:
        pytrends.build_payload([keyword], timeframe='today 5-y')
        data = pytrends.interest_over_time()
        print(data)  # 한글 출력
        time.sleep(60)
    except Exception as e:
        print(f"에러 발생: {keyword} - {e}")
        time.sleep(120)

import sys
import io

# 출력 스트림의 기본 인코딩 설정
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# 테스트 출력
print("한글 테스트")

from pytrends.request import TrendReq
import pandas as pd
import matplotlib.pyplot as plt

# pytrends 객체 생성
pytrends = TrendReq(hl='ko', tz=360)

# 실시간 급상승 검색어 가져오기
trending_searches = pytrends.trending_searches(pn='south_korea')
keywords = trending_searches[0].tolist()[:5]  # 상위 5개의 급상승 검색어
print("실시간 급상승 검색어:", keywords)
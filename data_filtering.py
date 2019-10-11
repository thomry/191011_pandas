import seaborn as sns

tips = sns.load_dataset('tips')
# data 수 확인
print(tips['size'].value_counts())
# 30번 이상의 주문이 있는 테이블을 추려 데이터 분석하기위한 필터링
tips_filtered = tips.\
    groupby('size').\
    filter(lambda x: x['size'].count() >= 30)
# 확인
print(tips_filtered['size'].value_counts())

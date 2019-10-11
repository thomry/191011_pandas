import pandas as pd
import seaborn as sns
import numpy as np

# 표준점수를 계산하는 함수
def my_zscore(x):
    # .std() 표준점수 함수
    return (x-x.mean()) / x.std()

df = pd.read_csv('gapminder.tsv', sep='\t')

# lifeExp 열의 표준점수를 계산
transform_z = df.groupby('year').lifeExp.transform(my_zscore)

# 랜덤으로 10개의 행 데이터를 가져옴
np.random.seed(42)
tips_10 = sns.load_dataset('tips').sample(10)
# total_bill 열의 값 4개를 임의로 선택해 누락값으로 변경
tips_10.loc[np.random.permutation(tips_10.index)[:4], 'total_bill'] = np.NaN
print(tips_10)

# 단, tips_10의 데이터는 여성보다 남성이 많으므로 여성데이터를 훼손시키지않기 위해서, 성별 구별해야함
# 남성과 여성의 누락값을 알아보기
count_sex = tips_10.groupby('sex').count()
print(count_sex)
# 성별 구분한뒤 total_bill열의 데이터를 받아 평균값 구하는 함수
def fill_na_mean(x):
    avg = x.mean()
    return x.fillna(avg)
total_bill_group_mean = tips_10.groupby('sex').total_bill.transform(fill_na_mean)
tips_10['fill_total_bill'] = total_bill_group_mean
print(tips_10)
import pandas as pd
import numpy as np

df                   = pd.read_csv('gapminder.tsv', sep='\t')
# year기준으로 데이터 그룹화한 다음 lifeExp 열의 평균을 구함
avg_life_exp_by_year = df.groupby('year').lifeExp.mean()
# year열의 데이터를 중복없이 추출
years = df.year.unique()
# 연도별로 평균값을 구함(반영)
y1952      = df.loc[df.year == 1952, :]
y1952_mean = y1952.lifeExp.mean()

y1957      = df.loc[df.year == 1957, :]
y1957_mean = y1957.lifeExp.mean()

y1962      = df.loc[df.year == 1962, :]
y1962_mean = y1962.lifeExp.mean()

y2007      = df.loc[df.year == 2007, :]
y2007_mean = y2007.lifeExp.mean()

# 결합
df2 = pd.DataFrame({'year':[1952,1957,1962,2007],
                    '':[y1952_mean,y1957_mean,y1962_mean,y2007_mean]})
print(df2)

# 입력받은 열의 평균값 구하는 함수
def my_mean(values):
    n = len(values)
    sum = 0
    for value in values:
        sum += value
    return sum / n
agg_my_mean = df.groupby('year').lifeExp.agg(my_mean)
print(agg_my_mean)

# 2개의 인잣값을 받아 처리하는 함수 만들기
def my_mean_diff(values, diff_value):
    n   = len(values)
    sum = 0
    for value in values:
        sum += value
    mean = sum / n
    return mean - diff_value

# 연도별 수명에서 전체 평균 수명을 뺀 값 구하기
global_mean = df.lifeExp.mean()
# agg는 group간에 함수를 적용하는 함수
agg_my_diff = df.groupby('year').lifeExp.agg(my_mean_diff, diff_value=global_mean)
print(agg_my_diff)

# 0이 아닌 값 개수, 평균, 표준편차 계산
gdf      = df.groupby('year').lifeExp.agg([np.count_nonzero, np.mean, np.std])
# 집계 메서드를 딕셔너리로 담아 전달
gdf_dict = df.groupby('year').agg({'lifeExp':'mean', 'pop':'median', 'gdpPercap':'median'})
print(gdf_dict)
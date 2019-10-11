import pandas as pd
import seaborn as sns
import numpy as np

# 제곱함수
def my_sq(x):
    return x ** 2
# n 제곱 함수
def my_exp(x, n):
    return x ** n
def print_div(x):
    print('-'*50)
    print()

df = pd.DataFrame({'a':[10, 20, 30], 'b':[20, 30, 40]})

# 함수 apply로 응용해보기
print(df['a'] ** 2)
sq = df['a'].apply(my_sq)
print(sq)
ex = df['a'].apply(my_exp, n=2)
print(ex)
print_div('')

# 새로운 함수
def print_me(x):
    print(x)

# axis 0은 열방향. 1은 행방향.
print(df.apply(print_me, axis=0))
print_div('')

# 인자값 3개 받는 함수 만들기
def avg_3(x, y, z):
    return (x+y+z) / 3

# print(df.apply(avg_3)) => 인잣값이 1개이므로 error
# error를 고치기위해 새로 함수 생성
def avg_3_apply(col):
    x = col[0]
    y = col[1]
    z = col[2]
    return (x + y + z) / 3
# error 안남
print(df.apply(avg_3_apply))
print_div('')

# for 구문으로 함수 만들기
def avg_3_apply(col):
    sum = 0
    for item in col:
        sum += item
    return sum / df.shape[0]
# 이 함수를 사용하면 행방향 데이터를 처리하는 함수도 만들 수 있음
def avg_2_apply(row):
    sum = 0
    for item in row:
        sum += item
    return sum / df.shape[1]

print(df.apply(avg_3_apply))
print(df.apply(avg_2_apply, axis=1))
print_div('')

titanic = sns.load_dataset('titanic')

def count_missing(vec):
    # 누락값 유무 판단
    null_vec   = pd.isnull(vec)
    # 누락값 세기
    null_count = np.sum(null_vec)
    return null_count

cmis_col = titanic.apply(count_missing)
print(cmis_col)
print_div('')

# 누락값 비율 계산함수 만들기
def prop_missing(vec):
    num = count_missing(vec)
    dem = vec.size
    return num / dem
pmis_col = titanic.apply(prop_missing)
print(pmis_col)
print_div('')

# 데이터 비율 구하는 함수 만들기
def prop_complete(vec):
    return 1 - prop_missing(vec)

cmis_row = titanic.apply(count_missing, axis=1)   # 행의 누락값
pmis_row = titanic.apply(prop_missing, axis=1)    # 행의 누락값의 비율
pcom_row = titanic.apply(prop_complete, axis=1)   # 행의 누락값이 아닌 비율

# 누락값 개수를 구하여 titanic dataframe에 추가
titanic['num_missing'] = titanic.apply(count_missing, axis=1)
print(titanic.head())
# 누락값이 있는 데이터만 따로 모아서 볼 수 있음.
print(titanic.loc[titanic.num_missing > 1, :].sample(10))
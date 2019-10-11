import pandas as pd
import seaborn as sns

tips = sns.load_dataset('tips')
# 자료형을 문자열로 변환
tips['sex_str'] = tips['sex'].astype(str)
# 변환된 데이터 다시 원래대로 만드는 법
tips['total_bill'] = tips['total_bill'].astype(str)
tips['total_bill'] = tips['total_bill'].astype(float)

# 잘못 입력된 문자열 처리
tips_sub_miss = tips.head(10)
tips_sub_miss.loc[[1, 3, 5, 7], 'total_bill'] = 'missing'
# tips_sub_miss.obj[[1, 3, 5, 7], 'total_bill'] = 'missing'
# print(tips_sub_miss)

# total_bill열의 타입 확인시 일어나는 오류를 ignore로 무시
tips_sub_miss['total_bill'] = pd.to_numeric(tips_sub_miss['total_bill'], errors='ignore')
# errors값에 coerce로 설정하면 문자열이던 missing이 nan(누락값)이 됨.
tips_sub_miss['total_bill'] = pd.to_numeric(tips_sub_miss['total_bill'], errors='coerce')
# downcast는 정수,실수같은 자료형을 더 작은 형태로 만들때 사용하는 메서드. 64비트 -> 32비트
# 실수 예상 범위가 크지않다면 downcast하는 것이 좋음. (메모리가 줄어들기 때문에)
tips_sub_miss['total_bill'] = pd.to_numeric(tips_sub_miss['total_bill'], errors='coerce',downcast='float')

# 문자열을 카테고리로 변경
tips['sex'] = tips['sex'].astype('category')
print(tips.info())

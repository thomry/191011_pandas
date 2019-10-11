import seaborn as sns

# tips data집합에서 임의로 10개 데이터 추출
tips_10 = sns.load_dataset('tips').sample(10, random_state=42)
# grouped 이용해 평균구하기
grouped = tips_10.groupby('sex')
avgs = grouped.mean()
print(avgs)

# 성별이 여성인 데이터만 추출
female = grouped.get_group('Female')
# 성별 그룹을 for 구문으로 출력
for sex_group in grouped:
    print(sex_group)
# 기존 for 구문이 튜플이므로, 자세한 정보 추출
for sex_group in grouped:
    print('the type is: {}\n'.format(type(sex_group)))
    print('the length is: {}\n'.format(len(sex_group)))
    first_element = sex_group[0]
    print('the first element is: {}\n'.format((first_element)))
    print('it has a type of: {}\n'.format(type(sex_group[0])))
    second_element = sex_group[1]
    print('the second element is: {}\n'.format((second_element)))
    print('it has a type of: {}\n'.format(type(sex_group[1])))
    print('what we have:')
    print(sex_group)

    break
print('-'*50)

# sex, time열을 기준으로 데이터 그룹화하고 평균값 구하기
bill_sex_time = tips_10.groupby(['sex','time'])
group_avg     = bill_sex_time.mean()
# reset_index 메서드 사용해 dataframe의 index 새로 부여
group_method = tips_10.groupby(['sex','time']).mean().reset_index()
print(group_method)
# as_index 사용해보기
group_param = tips_10.groupby(['sex','time'], as_index=False).mean()
print(group_param)

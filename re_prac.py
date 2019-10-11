import re

def re_prac(x):
    if x :
        print('match')
    else:
        print('no match')

tele_num = '1234567890'
# 길이가 10인 숫자를 확인.
m = re.match(pattern='\d\d\d\d\d\d\d\d\d\d', string=tele_num)
re_prac(m)

# 첫 번째 인덱스 반환
m.start()
# 마지막 인덱스 반환
m.end()
# 찾은 패턴의 첫 번째와 마지막 index 반환
m.span()
# 찾아낸 패턴 반환
m.group()

tele_num_spaces = '123 456 7890'
# \d\d\d\d\d\d\d\d\d\d == \d{10}
m = re.match(pattern='\d{10}', string=tele_num_spaces)
re_prac(m)

# 새로운 패턴
p = '\d{3}\s\d{3}\s\d{4}'
m = re.match(pattern=p, string=tele_num_spaces)
re_prac(m)

# 반각 기호로 구분
tele_num_space_paren_dash = '(123) 456-7890'
p = '\(?\d{3}\)?\s?\d{3}\s?-?\d{4}'
m = re.match(pattern=p, string=tele_num_space_paren_dash)
re_prac(m)
multi_str = """Guard: What? Ridden on a horse?
King Arthur: Yes!
Guard: You're using coconuts!
King Arthur: What?
Guard: You've got ... coconut[s] and you're bangin' 'em together.
"""

# splitlines 매서드
multi_str_split = multi_str.splitlines()
# 특정 문자열 가져오기
guard = multi_str_split[::2]

# replace 매서드로 guard: 문자열 빼보기
# Guard: 이 ''로 대체됨
guard = multi_str.replace('Guard: ', "").splitlines()[::2]
print(guard)

# 문자열 formatting
# {} = place holder
var = 'flesh wound'
s   = "It's just a {}!"
print(s.format(var))
# 홀더에 변수 지정해도 됨. place holder에 :,넣으면 숫자를 표현가능.
print("In 2005, Lu Chao of China recited {:,} digits of pi".format(67890))
# .4는 소숫점 이하의 숫자를 4개 출력. %사용시 백분율로 환산해 표현
print("I remember {0:.4} or {0:.4%} of what Lu Chao recited".format(7/67890))
# 42의 두자리값을 5자리수로 표현하되, 빈칸은 0으로 채워넣는 예문
print("My ID number is {0:05d}".format(42))

# % formatting
s = 'I only know %d digits of pi' % 7
print(s)
# string %s
print('Some digits of %(cont)s: %(value).2f' % {'cont':'e', 'value':2.718})
import re

p = re.compile("ca.e")
# ^ca   cafe car
# ca.e  case care
# ca$   kca goodca

def print_match(m):
    if m:
        print("m.group() : " ,  m.group())
        print("m.string : " ,  m.string)
        print("m.start() : " ,  m.start())
        print("m.end() : " ,  m.end())
        print("m.span() :", m.span())

    else :
        print("자료 없음")

m = p.match("make care")  # 주어진 문자열의 처음부터 일치하는지 확인 
print_match(m)

print("\n-------SEARCH------\n")
m = p.search("make care cate")  # 주어진 문자열 중에 일치하는 게 있는지 확인
print_match(m)

print("\n-------Findall------\n")
m = p.findall("make care cate")  # 일치하는 모든 것을 리스트 형태로 반환
print(m)
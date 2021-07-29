import requests

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55" }
res = requests.get("http://naver.com", headers = headers)

print("응답코드 : " , res.status_code)

# if res.status_codes == requests.codes.ok:
#     print("정상")
# else:
#     print("오류   [에러코드] : " , res.status_code)

res.raise_for_status()
print("정상")

with open("naver.html", "w", encoding="utf8") as f:
    f.write(res.text)
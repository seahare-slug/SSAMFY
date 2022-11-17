import json
# 시작 전 파이썬 형태의 주석 두줄 지우기

# json을 읽어서 정제
before = open("before_movies.json", "rt", encoding="UTF-8")
parsed = json.load(before)

new_json = []
movies = parsed["results"]

for movie in movies:
    new_json.append({"model": "movies.movie", "fields": movie})

# 정제한 데이터를 movies.json에 저장
# python manage.py dumpdata에 해당
after = open("after_movies.json", "w")
json.dump(new_json, after)
after.close()

# 인코딩 형식이 달라 저장(디코딩)시 특수문자가 표현이 안 되지만
# 다시 로드(UTF-8 형식으로 인코딩)하면 원래 형식 유지
# python manage.py loadda에 해당
datas = open("after_movies.json", "rt", encoding="UTF-8" )
output = json.load(datas)
print(output)

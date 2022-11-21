# npm install requests
import requests
import json

API_KEY = "616c881ba896937b008706b9a5e911d0"
MOVIE_API = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=ko-KR&page="
START_PAGE = 1
END_PAGE = 50

new_json = []

for page in range(START_PAGE, END_PAGE + 1):
    request_data = requests.get(f"{MOVIE_API}{page}").json()

    # json을 읽어서 정제
    before = open("before_movies.json", "w")
    json.dump(request_data, before)
    before.close()

    before1 = open("before_movies.json", "rt", encoding="UTF-8")
    parsed = json.load(before1)

    movies = parsed["results"]

    for movie in movies:
        new_json.append({"model": "movies.movie", "fields": movie})

# 정제한 데이터를 movies.json에 저장
# python manage.py dumpdata에 해당
after = open("after_movies.json", "w")
json.dump(new_json, after)
after.close()

# ============ 출력 test ====================================
# 인코딩 형식이 달라 저장(디코딩)시 특수문자가 표현이 안 되지만
# 다시 로드(UTF-8 형식으로 인코딩)하면 원래 형식 유지
# python manage.py loadda에 해당

# datas = open("after_movies.json", "rt", encoding="UTF-8")
# output = json.load(datas)
# print(len(output))

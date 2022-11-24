# SSAMFY (**S**eungkyu **S**ongsub **A**nd **M**ovie **F**or **Y**ou)

![shark](./readme-asset/img/shark_profile)

### 팀장 유승규

- **Vue Component 설계 및 routing**
- **프로젝트 관리 및 UI 데이터 개선**
- ERD 작성
- Django 기능 개선

#### 연혁

>**충남대학교 경제학과 학사 취득 22.02**
>>**현 SSAFY 8기**

<br/>

```
<!-- 회고 -->

<ul>
  <li></li>
  <li></li>
  <li></li>
  <li></li>
</ul>

<p></p>
```
<br/>

![song](./readme-asset/img/song_profile)

### 팀원 김송섭

- **UI/UX**
- **Django 서버 관리 및 유지보수**
- **데이터 정제**
- Django DB - Vue 연동
- CSS 구성 및 개선

#### 연혁

>**국립경상대학교 항공우주 및 소프트웨어 공학과 학사 취득 22.02**
>>**현 SSAFY 8기**

<br/>

```
<!-- 회고 -->

<ul>
  <li>사용자가 원하는 정보를 보여주되 함부로 장르를 배제하지 않도록 노력하였습니다.</li>
  <li>사용자가 관심있는 영화를 따로 관리할 수 있도록 노력하였습니다.</li>
  <li>사용자가 어려워하지 않게 심플한 구조를 통해 기능을 표현하였습니다.</li>
  <li>사용자가 필요하면 영화의 정보를 더욱 상세하게 볼 수 있도록 노력하였습니다.</li>
</ul>

<p>평소 공부하던 내용을 실제 서비스를 </p>
```
#
## 대표 서비스
- 사용자의 좋아요를 통한 영화 목록 관리
- 좋아요를 통한 알고리즘 기반 영화 추천
#
## 핵심 기능
- 영화 추천 알고리즘
  - 각 영화에 좋아요 버튼을 통해 사용자의 좋아요 정보를 수집한다.
  - 영화에 해당하는 장르에 가중치를 주고 좋아요의 수에 따라 점수를 합산한다.
  - 합산한 점수를 기준으로 높은 점수대를 모아 랜덤으로 표시한다.
  - 각 장르마다 어느정도 가중치를 가지고 있으므로 좋아요한 장르에 편향된 데이터들이 아닌 균형있는 영화를 보여줄 수 있다.
- 필터 기능
  - 영화의 투표 수, 평점 등을 토대로 고전 명작 / 독립 영화를 추려서 사용자가 원하는 정보만 보여준다
#
### How to Start
- requirements
  - Python 3.9.x
  - Django 3.2.x
  - Node.js 16.x
  - Vue 2

<br/>

- Vue (front)
  - final-pjt/final-pjt-front
    - `$ npm install`
    - `$ npm run serve`

- Django (back)
  - final-pjt/final-pjt-back
    - `$ pip install -r requirements`
    - `$ python manage.py makemigrations`
    - `$ python manage.py migrate`
    - `$ python manage.py loaddata genres.json after_movies.json`
    - `$ python manage.py runserver`
#
### ERD
![ERD](./readme-asset/img/ERD.PNG)

### Component
![components-structure](./readme-asset/img/component.PNG)

<br/>

## HomeView
![HomeView](./readme-asset/img/HomeView.PNG)

## RecommendView
![RecommendView](./readme-asset/img/RecommendView.PNG)

## ProfileView
![ProfileView](./readme-asset/img/ProfileView.PNG)

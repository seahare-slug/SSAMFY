# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, LikedSerializer
from .models import User, Movie

@api_view(["POST"])
def signup(request):
    # 비밀번호, 비밀번호 확인
    password = request.data.get("password")
    password_confirm = request.data.get("passwordConfirmation")
    # 비밀번호가 일치하지 않을때
    if password != password_confirm:
        return Response({"error : 비밀번호가 일치하지 않습니다!"}, status=status.HTTP_400_BAD_REQUEST)
    serializer = UserSerializer(data=request.data)

    # 데이터가 유효한지 검증
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        # 사용자의 암호를 해쉬함수를 통해 바꿔줌(암호화)
        user.set_password(request.data.get("password"))
        # 바꾼 비밀번호로 다시 저장
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["GET"])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def liked(request, movie_id):
    username = request.data["username"]
    movie = Movie.objects.get(pk=movie_id)
    user = User.objects.get(username=username)
    # 만약 username에서 해당 DB에 일치하는 movie_id가 없으면 추가, 있으면 제거
    if request.method == "POST":
        if user.liked_movie.filter(pk=movie_id).exists():
            user.liked_movie.remove(movie)
        else:
            user.liked_movie.add(movie)
    serializer = LikedSerializer(user)
    return Response(serializer.data)

@api_view(["GET"])
def liked_set(request, username):
    user = User.objects.get(username=username)
    serializer = LikedSerializer(user)
    return Response(serializer.data)

@api_view(["POST"])
def profile(request):
    username = request.data.get("username")
    return Response(username)
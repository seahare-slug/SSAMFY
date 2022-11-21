# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, LikedSerializer
from django.contrib.auth import get_user_model
from .models import User

# 회원가입 요청
@api_view(["POST"])
def signup(request):
    # 비밀번호, 비밀번호 확인
    password = request.data.get("password")
    password_confirm = request.data.get("passwordConfirmation")

    # 비밀번호가 일치하지 않을때
    if password != password_confirm:
        return Response(
            {"error : 비밀번호가 일치하지 않습니다!"}, status=status.HTTP_400_BAD_REQUEST
        )

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
    
# @api_view(["POST"])
# def liked(request):
#     username = request.data["likedData"]["username"]
#     liked_movie_id = request.data["likedData"]["liked_movie_id"]
    
#     user = User.objects.get(username=username, liked_movie=liked_movie_id)
#     if user:
#         pass
#     else:
#         serializer = LikedSerializer(request.data)
#         return Response(data=serializer.data)

@api_view(["POST"])
def profile(request):
    print(request.data)
    username = request.data.get("username")
    print(username)
    print("======================하이============")
    return Response(username)

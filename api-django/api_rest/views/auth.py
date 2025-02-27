from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.authtoken.models import Token

User = get_user_model()

@api_view(["POST"])
def Login(request):
    email = request.data.get("email")
    password = request.data.get("password")

    if not email:
        return Response({"email": "O campo e-mail é obrigatório."}, status=status.HTTP_400_BAD_REQUEST)
    
    if not password:
        return Response({"password": "O campo senha é obrigatório."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({"email": "E-mail inexistente."}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(username=email, password=password)
    
    if user is None:
        return Response({"password": "Senha inválida."}, status=status.HTTP_400_BAD_REQUEST)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key}, status=status.HTTP_200_OK)

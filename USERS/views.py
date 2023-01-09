from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import userserializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .models import users
import jwt
import datetime


# Create your views here.
class form(APIView):
    def get(self, request):
        return render(request, 'form.html')


class register(APIView):
    def post(self, request):
        print(request.data)
        S = userserializer(data=request.data)
        S.is_valid(raise_exception=True)
        S.save()
        return Response(S.data)


class LogIn(APIView):
    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]
        user = users.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed("invalid email")
        if not user.check_password(password):
            raise AuthenticationFailed("invalid password")

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, 'secret', algorithm='HS256')
        res = Response()
        res.set_cookie(key="jwt", value=token, httponly=True)
        res.data = {
            'jwt': token
        }
        return res


class profile(APIView):
    def get(self, request):
        token = request.COOKIES.get("jwt")
        if not token:
            raise AuthenticationFailed("Token not found")
        try:
            payload = jwt.decode(token, "secret", algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Authentication failed")

        user = users.objects.filter(id=payload['id']).first()
        S = userserializer(user, context={"request": request})
        print(S.data)
        return Response(S.data)


class logout(APIView):
    def get(self, request):
        res = Response()
        res.delete_cookie('jwt')
        res.data = {
            "status": "logged_out"
        }
        return res

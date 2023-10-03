from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import *
from django.contrib.auth.models import User
from rest_framework.validators import ValidationError 
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from django.core.mail import BadHeaderError, send_mail


class Register(APIView):
    def post(self, request , format=None): 
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            return Response({'access_token':access_token , 'msg':'Register successfully ','register_data':serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
class LoginApi(APIView):
    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)  
        try:
            user = User.objects.get(username=serializer.data.get('username'))
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        password = user.check_password(serializer.data.get('password'))
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        if not password:
            raise ValidationError({'password':'invalid password'})     
        return Response({'message': 'Login successful','access_token':access_token}, status=status.HTTP_200_OK)
    
    

@api_view(['POST'])
def create(request):
    user = request.user 
    subject = 'Assignment work have to complete todays anyhow '
    message = "I have to complete assignmet work "
    recipient_list = ['mk2648054@gmail.com','mukeshcse61@gmail.com']
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        send_mail(subject, message, 'mk2648054@gmail.com', recipient_list)
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        return Response({'message': 'Email sent successfully.','access_token':access_token,'data':'data created successfully','created_data':serializer.data})
    return Response(serializer.errors)


@api_view(['GET'])
def get(request):
    user = request.user
    pst = Post.objects.all()
    serializer = PostSerializer(pst,many=True) 
    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)
    return Response({'serialized_data':serializer.data,'access_token':access_token})

@api_view(['PATCH'])
def partial_update(request,pk):
    user = request.user
    pst = Post.objects.get(pk=pk)
    serializer = PostSerializer(pst, data=request.data , partial=True) 
    if serializer.is_valid():
        serializer.save()
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        return Response({'updated_data':serializer.data,'updated-data':'data has partially updated successfully','access_token':access_token})
    return Response(serializer.errors)



@api_view(['PUT'])
def fully_update(request,pk):
    user = request.user
    pst = Post.objects.get(pk=pk)
    serializer = PostSerializer(pst, data=request.data) 
    if serializer.is_valid():
        serializer.save()
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        return Response({'updated_data':serializer.data,'updated-data':'data has partially updated successfully','access_token':access_token})
    return Response(serializer.errors)


@api_view(['DELETE'])
def deleted(request,pk):
    user = request.user
    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)
    pst = Post.objects.get(pk=pk) 
    pst.delete()
    return Response({'msg':'data has deleted','access_tokne':access_token})




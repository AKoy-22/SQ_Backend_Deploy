#from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import ScribbleQuest_User, Maths_Score, Words_Score
from .serializers import UserSerializer 
from django.contrib.auth import authenticate

# Create your views here.

#api for getting all data from db
@api_view(['GET'])
def getData(request):
    items = ScribbleQuest_User.objects.all()
    serializer = UserSerializer(items, many=True)
    return Response(serializer.data)

#api for creating a new user 
@api_view(['POST'])
def addUser(request):
    serializer = UserSerializer(data=request.data) #data sent from the frontend 
    if serializer.is_valid():
        serializer.save()
    else:
        serializer.error_messages
        print("there was serializer error")
    return Response(serializer.data)

#api for login authentication 

@api_view(['POST'])
def loginAuth(request):
    email = request.data.get('email')
    password = request.data.get('password')
    print(request.data)
    print(email)
    print(password)
    # Check if email exists in the database
    try:
        user = ScribbleQuest_User.objects.get(email=email)
    except ScribbleQuest_User.DoesNotExist:
        return Response({'message': 'Email does not exist'}, status=400)

    # Authenticate the user
    authenticated_user = authenticate(username=email, password=password)
    if authenticated_user is None:
        return Response({'message': 'Invalid password'}, status=400)

    # Successful login
    return Response({'message': 'Login successful'})

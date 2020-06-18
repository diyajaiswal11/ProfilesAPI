from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import UserProfile, Favourite
from .serializers import UserProfileSerializer,FavouriteSerializer, FavouriteSerializer1
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets , status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


@csrf_exempt
def loginreg(request):
    if request.method=='GET':
        data=JSONParser().parse(request)
        email1=data['email']
        if UserProfile.objects.filter(email=email1).exists():
            obj=UserProfile.objects.get(email=email1)
            msg={"user_id":obj.pk, "login_type":"signin"}
        else:
            msg={"user_id":"not registered", "login_type":"signup"}
        return JsonResponse(data=msg,status=200)

    if request.method=='POST':
        data=JSONParser().parse(request)
        userid=data['userid']
        password1=data['password']
        if UserProfile.objects.filter(pk=userid).exists():
            obj=UserProfile.objects.get(pk=userid)
            print(obj.password)
            if obj.check_password(password1):
                msg={'message':'login successful'}
            else:
                print("1")
                msg={'message':'failed'}
        else:
            print("2")
            msg={'message':'failed'}
        return JsonResponse(data=msg,status=200)




@csrf_exempt
def profile(request):
    if request.method=='GET':
        users=UserProfile.objects.all()
        serializer=UserProfileSerializer(users,many=True)
        return JsonResponse(serializer.data,safe=False)
    
    if request.method=='POST':
        data=JSONParser().parse(request)
        serializer=UserProfileSerializer(data=data)

        if serializer.is_valid():
            instance=serializer.save()
            instance.set_password(instance.password)
            instance.save()
            return JsonResponse(serializer.data,status=201)

        return JsonResponse(serializer.errors,status=400)

@csrf_exempt
def user_detail(request):
    if request.method=='GET':
        data=JSONParser().parse(request)
        user_id=data['user_id']
        user=UserProfile.objects.get(pk=user_id)
        serializer=UserProfileSerializer(user) 
        fav=Favourite.objects.filter(userid=str(user_id))
        serializer1=FavouriteSerializer1(fav,many=True)
        msg={
            "User":serializer.data,
            "Favourites":serializer1.data
        }
        return JsonResponse(data=msg,status=200)
        
    

@csrf_exempt
def favourite(request):
    if request.method=='GET':
        users=Favourite.objects.all()
        serializer=FavouriteSerializer(users,many=True)
        return JsonResponse(serializer.data,safe=False)


    elif request.method=='POST':
        data=JSONParser().parse(request)
        serializer=FavouriteSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)

        return JsonResponse(serializer.errors,status=400)

    elif request.method=='DELETE':
        data=JSONParser().parse(request)
        userid1=data['userid']
        category1=data['category']
        deletedata=Favourite.objects.get(userid=userid1,category=category1)
        deletedata.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)




    



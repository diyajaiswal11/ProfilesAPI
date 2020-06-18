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
def profile(request):
    if request.method=='GET':
        users=UserProfile.objects.all()
        serializer=UserProfileSerializer(users,many=True)
        return JsonResponse(serializer.data,safe=False)

    elif request.method=='POST':
        data=JSONParser().parse(request)
        serializer=UserProfileSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)

        return JsonResponse(serializer.errors,status=400)

@api_view(['GET'])
def user_detail(request,pk):
    try:
        user=UserProfile.objects.get(pk=pk)

    except UserProfile.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serializer=UserProfileSerializer(user) 
        fav=Favourite.objects.filter(userid=str(pk))
        serializer1=FavouriteSerializer1(fav,many=True)
        return Response({
            "User":serializer.data,
            "Favourites":serializer1.data
        })
    

@csrf_exempt
def favourite(request):
    if request.method=='GET':
        users=Favourite.objects.all()
        serializer=FavouriteSerializer(users,many=True)
        return JsonResponse(serializer.data,safe=False)


    elif request.method=='POST':
        data=JSONParser().parse(request)
        #print(data['userid'])
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




    



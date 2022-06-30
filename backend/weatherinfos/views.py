from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
from .serializers import WeatherSerializer
from .models import Weather
from rest_framework.response import Response
import datetime

# Create your views here.
@api_view(['GET', 'POST'])
def index(request):


    def get_weather():
        '''
        어제 날씨 데이터 다 받아서 넘기고 싶음
        now값이랑 created_at값이랑 비교해야 함
        '''
        now = datetime.datetime.now()
        now_hour = now.hour
        weather = Weather.objects.order_by('-created_at')
        if len(weather) > 24:
            weather = Weather.objects.order_by('-created_at')[now_hour + 1: now_hour + 25]
            serializer = WeatherSerializer(weather, many=True)
            return Response(serializer.data)
        else:
            weather = Weather.objects.order_by('-created_at')[1]
            serializer = WeatherSerializer(weather)
            return Response([serializer.data])


    def post_weather():
        print('POST요청 받음')
        post_serializer = WeatherSerializer(data=request.data)
        if post_serializer.is_valid(raise_exception=True):
            post_serializer.save()
            return Response(post_serializer.data)


    if request.method == 'POST':
        return post_weather()
    elif request.method == 'GET':
        return get_weather()
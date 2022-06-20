from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
from .serializers import WeatherSerializer
from .models import Weather
from rest_framework.response import Response

# Create your views here.
@api_view(['GET', 'POST'])
def index(request):


    def get_weather():
        weather = Weather.objects.order_by('-created_at')[0]
        serializer = WeatherSerializer(weather)
        print(type(serializer.data.get('created_at')))
        return Response(serializer.data)
    

    def post_weather():
        weather = Weather.objects.order_by('-created_at')[0]
        serializer = WeatherSerializer(weather)

        post_serializer = WeatherSerializer(data=request.data)
        if post_serializer.is_valid(raise_exception=True):

            post_serializer.save()
            return Response(post_serializer.data)


    if request.method == 'POST':
        return post_weather()
    elif request.method == 'GET':
        return get_weather()
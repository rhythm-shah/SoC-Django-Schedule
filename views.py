from django.shortcuts import render
from rest_framework import viewsets
from .models import Time, Day, Schedule, Food
#User
from .serializers import TimeSerializer, DaySerializer, ScheduleSerializer, FoodSerializer
#UserSerializer

class TimeView(viewsets.ModelViewSet):
    queryset = Time.objects.all()
    serializer_class = TimeSerializer

class DayView(viewsets.ModelViewSet):
    queryset = Day.objects.all()
    serializer_class = DaySerializer

class FoodView(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class ScheduleView(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

#class UserView(viewsets.ModelViewSet):
#    queryset = User.objects.all()
#    serializer_class = UserSerializer




















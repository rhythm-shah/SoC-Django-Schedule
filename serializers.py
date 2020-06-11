from rest_framework import serializers
from .models import Time, Day, Schedule, Food
#User

class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = ('url', 'name')

class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = ('url', 'name')

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ('url', 'name')

class ScheduleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Schedule
        fields = ('id', 'url', 'name', 'time', 'day', 'food')

#class UserSerializer(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = User
#        fields = ('id', 'url', 'user_id', 'schedule')

















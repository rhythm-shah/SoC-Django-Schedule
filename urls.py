from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('time', views.TimeView)
router.register('day', views.DayView)
router.register('food', views.FoodView)
router.register('schedule', views.ScheduleView)
#router.register('user', views.UserView)

urlpatterns = [
    path('', include(router.urls))
]
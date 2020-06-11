from django.db import models

class Time(models.Model):
    name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class Day(models.Model):
    name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class Schedule(models.Model):
    name = models.CharField(max_length=100, blank=True)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    time = models.ForeignKey(Time, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

#class User(models.Model):
#    user_id = models.CharField(max_length=1000)
#    schedule = models.ManyToManyField(Schedule)

#    def __str__(self):
#        return self.user_id
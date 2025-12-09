from django.db import models

# Placeholder models for MongoDB collections (Django ORM is not used with djongo for these, but required for admin/tests)
class User(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField()
    # Add more fields as needed
    class Meta:
        managed = False
        db_table = 'users'

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.JSONField(default=list)
    class Meta:
        managed = False
        db_table = 'teams'

class Activity(models.Model):
    user = models.CharField(max_length=150)
    type = models.CharField(max_length=100)
    duration = models.IntegerField()
    date = models.DateField()
    class Meta:
        managed = False
        db_table = 'activities'

class Leaderboard(models.Model):
    user = models.CharField(max_length=150)
    score = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'leaderboard'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    difficulty = models.CharField(max_length=50)
    class Meta:
        managed = False
        db_table = 'workouts'

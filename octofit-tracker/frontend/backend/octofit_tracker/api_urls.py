from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_root, name='api_root'),
    path('users/', views.users_list, name='users-list'),
    path('teams/', views.teams_list, name='teams-list'),
    path('activities/', views.activities_list, name='activities-list'),
    path('leaderboard/', views.leaderboard_list, name='leaderboard-list'),
    path('workouts/', views.workouts_list, name='workouts-list'),
]

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
from django.http import JsonResponse

# Dummy data for demonstration
@api_view(['GET'])
def api_root(request):
    return Response({
        'users': '/users/',
        'teams': '/teams/',
        'activities': '/activities/',
        'leaderboard': '/leaderboard/',
        'workouts': '/workouts/',
    })

@api_view(['GET'])
def users_list(request):
    # Replace with MongoDB query
    return Response([])

@api_view(['GET'])
def teams_list(request):
    return Response([])

@api_view(['GET'])
def activities_list(request):
    return Response([])

@api_view(['GET'])
def leaderboard_list(request):
    return Response([])

@api_view(['GET'])
def workouts_list(request):
    return Response([])

from rest_framework import serializers

# User Serializer
class UserSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    # Add more fields as needed

# Team Serializer
class TeamSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=100)
    members = UserSerializer(many=True, required=False)

# Activity Serializer
class ActivitySerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    user = UserSerializer()
    type = serializers.CharField(max_length=100)
    duration = serializers.IntegerField()
    date = serializers.DateField()

# Leaderboard Serializer
class LeaderboardSerializer(serializers.Serializer):
    user = UserSerializer()
    score = serializers.IntegerField()

# Workout Serializer
class WorkoutSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    difficulty = serializers.CharField(max_length=50)

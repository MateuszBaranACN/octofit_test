from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete all existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users (super heroes)
        marvel_heroes = [
            {'username': 'IronMan', 'email': 'ironman@marvel.com'},
            {'username': 'CaptainAmerica', 'email': 'cap@marvel.com'},
            {'username': 'Thor', 'email': 'thor@marvel.com'},
        ]
        dc_heroes = [
            {'username': 'Superman', 'email': 'superman@dc.com'},
            {'username': 'Batman', 'email': 'batman@dc.com'},
            {'username': 'WonderWoman', 'email': 'wonderwoman@dc.com'},
        ]
        users = [User(**data) for data in marvel_heroes + dc_heroes]
        for user in users:
            user.save()

        # Create teams
        marvel_team = Team(name='Marvel', members=[u.username for u in users[:3]])
        dc_team = Team(name='DC', members=[u.username for u in users[3:]])
        marvel_team.save()
        dc_team.save()

        # Create activities
        activities = [
            Activity(user='IronMan', type='Running', duration=30, date='2025-12-01'),
            Activity(user='Superman', type='Swimming', duration=45, date='2025-12-02'),
        ]
        for activity in activities:
            activity.save()

        # Create leaderboard
        leaderboard_entries = [
            Leaderboard(user='IronMan', score=100),
            Leaderboard(user='Superman', score=120),
        ]
        for entry in leaderboard_entries:
            entry.save()

        # Create workouts
        workouts = [
            Workout(name='Pushups', description='Do 20 pushups', difficulty='Easy'),
            Workout(name='Sprints', description='Run 5 sprints', difficulty='Medium'),
        ]
        for workout in workouts:
            workout.save()

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))

from django.test import TestCase
from django.urls import reverse

class ApiRootTest(TestCase):
    def test_api_root(self):
        response = self.client.get(reverse('api_root'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
        self.assertIn('workouts', response.data)

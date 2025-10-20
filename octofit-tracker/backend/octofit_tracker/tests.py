from rest_framework.test import APITestCase
from django.urls import reverse
from .models import User, Team, Activity, Leaderboard, Workout

class APIRootTest(APITestCase):
	def test_api_root(self):
		url = reverse('api_root')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)

class UserTests(APITestCase):
	def test_list_users(self):
		url = reverse('user-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)

class TeamTests(APITestCase):
	def test_list_teams(self):
		url = reverse('team-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)

class ActivityTests(APITestCase):
	def test_list_activities(self):
		url = reverse('activity-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)

class LeaderboardTests(APITestCase):
	def test_list_leaderboard(self):
		url = reverse('leaderboard-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)

class WorkoutTests(APITestCase):
	def test_list_workouts(self):
		url = reverse('workout-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)

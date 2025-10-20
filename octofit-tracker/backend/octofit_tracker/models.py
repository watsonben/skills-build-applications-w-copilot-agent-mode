from djongo import models

class User(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(unique=True)
	team = models.CharField(max_length=50)
	def __str__(self):
		return self.name

class Team(models.Model):
	name = models.CharField(max_length=100, unique=True)
	def __str__(self):
		return self.name

class Activity(models.Model):
	user_email = models.EmailField()
	activity = models.CharField(max_length=100)
	duration = models.IntegerField()
	def __str__(self):
		return f"{self.user_email} - {self.activity}"

class Leaderboard(models.Model):
	team = models.CharField(max_length=100)
	points = models.IntegerField()
	def __str__(self):
		return f"{self.team}: {self.points}"

class Workout(models.Model):
	name = models.CharField(max_length=100)
	difficulty = models.CharField(max_length=50)
	def __str__(self):
		return self.name

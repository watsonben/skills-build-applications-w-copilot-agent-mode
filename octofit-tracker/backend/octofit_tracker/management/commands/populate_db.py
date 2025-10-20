from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from django.conf import settings
from pymongo import MongoClient

# Sample data
USERS = [
    {"name": "Superman", "email": "superman@dc.com", "team": "DC"},
    {"name": "Batman", "email": "batman@dc.com", "team": "DC"},
    {"name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "DC"},
    {"name": "Iron Man", "email": "ironman@marvel.com", "team": "Marvel"},
    {"name": "Captain America", "email": "cap@marvel.com", "team": "Marvel"},
    {"name": "Black Widow", "email": "widow@marvel.com", "team": "Marvel"},
]

TEAMS = [
    {"name": "Marvel"},
    {"name": "DC"},
]

ACTIVITIES = [
    {"user_email": "superman@dc.com", "activity": "Flying", "duration": 120},
    {"user_email": "ironman@marvel.com", "activity": "Suit Training", "duration": 90},
]

LEADERBOARD = [
    {"team": "Marvel", "points": 300},
    {"team": "DC", "points": 250},
]

WORKOUTS = [
    {"name": "Strength Training", "difficulty": "Hard"},
    {"name": "Cardio Blast", "difficulty": "Medium"},
]

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Drop collections if they exist
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Insert test data
        db.users.insert_many(USERS)
        db.teams.insert_many(TEAMS)
        db.activities.insert_many(ACTIVITIES)
        db.leaderboard.insert_many(LEADERBOARD)
        db.workouts.insert_many(WORKOUTS)

        # Create unique index on email for users
        db.users.create_index([("email", 1)], unique=True)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))

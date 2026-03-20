from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Sample teams
        marvel = Team.objects.create(name='Marvel', members=['Iron Man', 'Captain America', 'Thor'])
        dc = Team.objects.create(name='DC', members=['Superman', 'Batman', 'Wonder Woman'])

        # Sample users
        User.objects.create(email='ironman@marvel.com', name='Tony Stark', team='Marvel', super_hero='Iron Man')
        User.objects.create(email='cap@marvel.com', name='Steve Rogers', team='Marvel', super_hero='Captain America')
        User.objects.create(email='thor@marvel.com', name='Thor Odinson', team='Marvel', super_hero='Thor')
        User.objects.create(email='superman@dc.com', name='Clark Kent', team='DC', super_hero='Superman')
        User.objects.create(email='batman@dc.com', name='Bruce Wayne', team='DC', super_hero='Batman')
        User.objects.create(email='wonderwoman@dc.com', name='Diana Prince', team='DC', super_hero='Wonder Woman')

        # Sample activities
        Activity.objects.create(user='Tony Stark', activity_type='Running', points=100, date='2026-03-20')
        Activity.objects.create(user='Steve Rogers', activity_type='Cycling', points=80, date='2026-03-19')
        Activity.objects.create(user='Thor Odinson', activity_type='Swimming', points=90, date='2026-03-18')
        Activity.objects.create(user='Clark Kent', activity_type='Running', points=110, date='2026-03-20')
        Activity.objects.create(user='Bruce Wayne', activity_type='Cycling', points=70, date='2026-03-19')
        Activity.objects.create(user='Diana Prince', activity_type='Swimming', points=95, date='2026-03-18')

        # Sample leaderboard
        Leaderboard.objects.create(team='Marvel', points=270)
        Leaderboard.objects.create(team='DC', points=275)

        # Sample workouts
        Workout.objects.create(name='Hero HIIT', description='High intensity interval training for heroes.', difficulty='Hard')
        Workout.objects.create(name='Power Yoga', description='Yoga for strength and flexibility.', difficulty='Medium')
        Workout.objects.create(name='Speed Run', description='Running workout for speed.', difficulty='Easy')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
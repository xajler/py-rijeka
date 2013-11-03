from django.db import models

SEASONS = (('13', '2013/14'),)

class Club(models.Model):
    name = models.CharField(max_length=64)
    image_name = models.CharField(max_length=128)
    is_current = models.BooleanField()

    def __str__(self):
        return self.name

class CalendarItem(models.Model):
    MATCH_TYPES = (('H', 'HNL'), ('U', 'UEFA'),  ('K', 'Kup'),)

    home_club = models.ForeignKey(Club, related_name='calendar_item_home_clubs')
    guest_club = models.ForeignKey(Club, related_name='calendr_item_guest_clubs')
    match_date = models.DateTimeField()
    match_type = models.CharField(max_length=1, choices=MATCH_TYPES, default='H')

    def __str__(self):
        return self.home_club.name + ' - ' + self.guest_club.name

class GameResult(models.Model):
    season = models.CharField(max_length=2, choices=SEASONS, default='13')
    number = models.IntegerField()
    date = models.DateTimeField()
    home_club = models.ForeignKey(Club, related_name='game_result_home_clubs')
    home_goals = models.IntegerField()
    guest_club = models.ForeignKey(Club, related_name='game_result_guest_clubs')
    guest_goals = models.IntegerField()

    def __str__(self):
        return self.home_club.name + ' - ' + self.guest_club.name

class LeagueTableItem(models.Model):
    season = models.CharField(max_length=2, choices=SEASONS, default='13')
    position = models.IntegerField()
    wins = models.IntegerField()
    draws = models.IntegerField()
    loses = models.IntegerField()
    goals_for = models.IntegerField()
    goals_against = models.IntegerField()
    points = models.IntegerField()
    club = models.ForeignKey(Club)

    def __str__(self):
        return self.club.name

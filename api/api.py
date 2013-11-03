from tastypie.resources import ModelResource
from api.models import Club, CalendarItem, GameResult, LeagueTableItem

class ClubResource(ModelResource):
    class Meta:
        queryset = Club.objects.all()
        resource_name = 'club'
        allowed_method = 'get'

class CalendarItemResource(ModelResource):
    class Meta:
        queryset = CalendarItem.objects.all()
        resource_name = 'calendar'
        allowed_method = 'get'

class GameResultResource(ModelResource):
    class Meta:
        queryset = GameResult.objects.all()
        resource_name = 'game-result'
        allowed_method = 'get'

class LeagueTableItemResource(ModelResource):
    class Meta:
        queryset = LeagueTableItem.objects.all()
        resource_name = 'league-table'
        allowed_method = 'get'

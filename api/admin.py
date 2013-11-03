from django.contrib import admin
from api.models import Club, CalendarItem, GameResult, LeagueTableItem

class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_current',)

class CalendarItemAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'match_date', 'match_type',)
    list_filter = ('home_club__name',)

class GameResultAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'home_goals', 'guest_goals', 'number', 'date')
    list_filter = ('home_club__name',)

class LeagueTableItemAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'wins', 'draws', 'loses', 'goals_for',
                    'goals_against', 'points')

admin.site.register(Club, ClubAdmin)
admin.site.register(CalendarItem, CalendarItemAdmin)
admin.site.register(GameResult, GameResultAdmin)
admin.site.register(LeagueTableItem, LeagueTableItemAdmin)

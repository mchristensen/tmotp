from django.contrib import admin
from tmotp.models import *

class CardAdmin(admin.ModelAdmin):
    ordering = ('title',)
    
class CardStatusAdmin(admin.ModelAdmin):
    ordering = ('card__title',)
    list_filter = ('status','game',)
    list_display = ('card_title', 'card_campaign_points', 'card_rest_cubes', 'card_issue','card_state','card_party','status','card_event_text')
    
admin.site.register(State)
admin.site.register(Issue)
admin.site.register(Card,CardAdmin)
admin.site.register(Status)
admin.site.register(CardStatus,CardStatusAdmin)
admin.site.register(Game)



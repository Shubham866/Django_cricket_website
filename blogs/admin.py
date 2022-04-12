from django.contrib import admin
from .models import article, Player,Nation , Match ,Run , Ball, player_match

# Register your models here.
admin.site.register(article)
admin.site.register(Player)
admin.site.register(Nation)
admin.site.register(Match)
admin.site.register(Run)
admin.site.register(Ball)
admin.site.register(player_match)


## admin.site.register(Nation)
# admin.site.register(Match)
# admin.site.register(Tournament)
# admin.site.register(Venue)

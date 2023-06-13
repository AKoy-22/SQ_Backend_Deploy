from django.contrib import admin

# Register your models here.
from .models import ScribbleQuest_User, Maths_Score, Words_Score
# Register your models here.

#extends ModelAdmin class

admin.site.register(ScribbleQuest_User)
admin.site.register(Maths_Score)
admin.site.register(Words_Score)

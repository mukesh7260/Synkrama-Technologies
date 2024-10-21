from django.contrib import admin

from .models import *

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display  = ['id','title','body','author']
    

admin.site.register(Mobile)
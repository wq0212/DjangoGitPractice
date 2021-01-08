from django.contrib import admin
from community.models import MainBoard
# Register your models here.

@admin.register(MainBoard)
class MainBoardAdmin(admin.ModelAdmin):
    list_display = ('id','title','contents')
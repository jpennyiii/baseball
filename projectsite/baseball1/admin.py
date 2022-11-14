from django.contrib import admin
from django.contrib.admin import display
from .models import Position, Person, Club
# from .models import Person
#, Person, Club, Play
@admin.register(Position)

class PositionAdmin(admin.ModelAdmin):
	list_display=("description",)
	search_fields=("description",)
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
	list_display=("firstname",)
	search_fields=("firstname",)	
@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
	list_display=("name",)
	search_fields=("name",)
# Register your models here.

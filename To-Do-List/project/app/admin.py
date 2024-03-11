from django.contrib import admin
from  .models import *
# Register your models here.

class TodolistAdmin(admin.ModelAdmin):
  list_display = ['user', 'item', 'is_completed', 'created','priority']
  list_filter = ['priority', ]

admin.site.register(Todolist, TodolistAdmin)
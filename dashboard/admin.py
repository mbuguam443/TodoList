from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_done', 'created_at')
    list_editable = ('is_done',)  # 👈 this makes 'is_done' editable in the list
    list_filter = ('is_done', 'created_at')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)

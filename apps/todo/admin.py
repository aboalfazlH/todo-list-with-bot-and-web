from django.contrib import admin
from .models import Todo,ToDoList


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):

    list_display = ('title','for_list','start_date','end_date','public','todo_type',)
    list_filter = ('for_list','end_date','start_date','public')
    readonly_fields = ('start_date','end_date')
    search_fields = ('title','description')
    date_hierarchy = 'end_date'
    ordering = ('-end_date',)

@admin.register(ToDoList)
class ToDoListAdmin(admin.ModelAdmin):
    '''Admin View for ToDoList'''

    list_display = ('name','for_user')
    list_filter = ('for_user',)
    readonly_fields = ('create_list_date',)
    search_fields = ('name',)
    date_hierarchy = 'create_list_date'
    ordering = ('-create_list_date',)
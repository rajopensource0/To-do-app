
from django.urls import path, include
from .views import (
		add_todo,
		complete_todo,
		delete_completed,
		delete_all,
		index
	)
urlpatterns = [
    path('', index, name = 'index'),
    path('add', add_todo, name = 'add'),
    path('complete/<todo_id>', complete_todo, name = 'complete'),
    path('deletecomplete', delete_completed, name = 'deletecomplete'),
path('deleteall', delete_all, name = 'deleteall')
]

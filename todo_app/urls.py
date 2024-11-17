from django.urls import path
from . import views

urlpatterns = [
    path('taskslist', views.todolist, name='taskslist'),
    path('updatetask/<int:task_id>', views.task_update, name='updatetask'),
    path('deletetask/<int:task_id>/', views.task_delete, name='deletetask'),
    path('donetask/<int:task_id>/', views.task_toggle_status, name='tasktoggle'),
    path('logout/', views.logout_view, name='logout')
]
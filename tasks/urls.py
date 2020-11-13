from django.urls import path
from . import views


urlpatterns = [
    path('', views.task_index, name='task_index'),
    path('update_task/<str:pk>/', views.update_task, name='update_task'),
    path('delete_task/<str:pk>', views.delete_task, name='delete_task'),
    path('done/', views.done_task, name='done_task')
]
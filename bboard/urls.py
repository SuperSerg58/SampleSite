from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_bboard, name='main_bboard'),
    path('<int:rubric_id>/', views.by_rubric, name='by_rubric'),
    path('add/', views.bb_create, name='add'),
    path('<pk>/delete/', views.bb_delete, name='delete')
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('blog/', views.post_list, name='post_list'),
    path('blog/post/<int:pk>/', views.post_detail, name='post_detail'),
    path('blog/new/', views.post_new, name='post_new'),
    path('blog/post/<pk>/edit', views.post_edit, name='post_edit'),
    path('blog/<pk>/delete', views.post_delete, name='post_delete'),
]
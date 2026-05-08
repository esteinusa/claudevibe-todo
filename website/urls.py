from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('todo/<int:pk>/toggle/', views.toggle_todo, name='toggle_todo'),
    path('todo/<int:pk>/delete/', views.delete_todo, name='delete_todo'),
    path('register/', views.register, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
]
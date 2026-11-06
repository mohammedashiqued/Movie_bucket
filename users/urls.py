from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.user,name='user'),
    path('login/', views.login,name='login'),
    path('logout/', views.logout,name='logout'),
    
]
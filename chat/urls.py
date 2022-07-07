from django.urls import path
from chat import views

urlpatterns = [
    path('', views.home, name='home'),
    path('fuck', views.test, name='hofdme'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('enter_room/<int:user1_id>/<int:user2_id>/', views.enter_room, name='enter_room'),
    # path('<str:room_name>/', views.room, name='room')
]

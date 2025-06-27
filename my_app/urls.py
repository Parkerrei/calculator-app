
from django.urls import path 
from .views import show_main, create_user, login_user, user_out, delete_user, delete

urlpatterns = [
    path('show_main/', show_main, name='show_main'),
    path('', create_user, name='create_user'),
    path('login_user/', login_user, name='login_user'),
    path('user_out/', user_out, name='user_out'),
    path('delete_user/', delete_user, name='delete_user'),
    path('delete/', delete, name='delete'),
]

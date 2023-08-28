from django.urls import path
from .views import signup, user_login, user_logout


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout')
]

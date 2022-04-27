from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('login_register/',views.log_reg,name='log-reg'),
    path('register/',views.register,name='register'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.logout_view,name='logout'),
    path('posts',views.posts,name='posts'),
    path('posts_creation/',views.posts_creation,name='posts_creation'),

]
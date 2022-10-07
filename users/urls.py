from django.urls import path
from django import urls
#from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
     path('login/', LoginView.as_view, {'template_name': 'users/login.html'}, name = 'login'),
     path('signup/',views.signup, name = 'signup'),
     path('posts/',views.posts, name = 'posts'),
     path('postform/',views.postform, name = 'postform'),
     #was url('path/ views.postform, name = postform)
     #url was changed to path in all url.py files 
     # from django.conf.urls import url was commented out in all url.py files. 
     #Bug fixed


]
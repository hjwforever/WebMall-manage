from django.conf.urls import url, include
from myapp import views

urlpatterns = [url(r'add_book$', views.add_book),
               url(r'get_book$', views.get_book),
               url(r'show_books$', views.show_books),
               url(r'add_user$', views.add_user),
               url(r'show_users$', views.show_users),
               url(r'login$', views.login),
               url(r'signin$', views.signin),
               url(r'signup$', views.signup),
               ]

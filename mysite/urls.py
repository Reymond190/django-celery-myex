from django.conf.urls import url
from django.urls import path, include
from mysite.core import views


urlpatterns = [
    url(r'^$', views.UsersListView.as_view(), name='users_list'),
    url(r'^generate/$', views.GenerateRandomUserView.as_view(), name='generate'),
    path('ray/',views.myview,name='once')
]

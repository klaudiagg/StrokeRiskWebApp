from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='index'),
    url(r'^results/', views.results, name='results'),
]

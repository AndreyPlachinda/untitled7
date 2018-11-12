from django.conf.urls import url, include
from landing import views

urlpatterns = [
    url(r'^landing/', views.lending, name="landing")
]


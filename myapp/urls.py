from django.urls import path
from myapp import views
from django.urls import include
from django.urls import path

app_name = 'myapp'

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'about/', views.about, name='about'),
    path(r'<int:top_no>/', views.detail, name='detail'),
]

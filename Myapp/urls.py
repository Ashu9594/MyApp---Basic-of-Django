from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('add',views.add, name='add'),
    path('about/',views.about, name='about'),
    
]
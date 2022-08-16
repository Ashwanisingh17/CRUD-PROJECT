from django.contrib import admin
from django.urls import path
from my_app.apps import MyAppConfig
from my_app import views

app_name = MyAppConfig.name

urlpatterns = [
    path('', views.index, name='index' ),
    path('add_show', views.add_show, name='add_show'),
    path('home/', views.home, name='home' ),
    # path('stuinfo/', views.student_details, name='student_details' ),
    # path('apioverview/', views.apioverview, name='apioverview' ),
    path('deletedata/<int:id>/', views.deletedata, name='deletedata' ),
    path('updatedata/<int:id>/', views.updatedata, name='updatedata' )

      
]


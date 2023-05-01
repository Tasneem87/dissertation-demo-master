from django.urls import path
from . import views
from . import sqlia

#  URL Config
urlpatterns = [
    path('hello/', views.say_hello),
    path('sqlia/get_all_person_details/<str:id>/', sqlia.sqlia_all_details),
    path('blocked/get_all_person_details/<str:id>/', sqlia.blocked_all_details),
    path('sqlia/sqlia_details_from_other_table/<str:id>/', sqlia.sqlia_details_from_other_table),
    path('blocked/sqlia_details_from_other_table/<str:id>/', sqlia.blocked_details_from_other_table),
    path('sqlia/get_city/<str:id>/', sqlia.sqlia_city) #http://127.0.0.1:8000/demo/sqlia/get_city/where%20tier%3D'tier2'%20and%20airquality%3E90/
]
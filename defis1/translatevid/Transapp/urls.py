from django.urls import path
from .views import Home,translate
urlpatterns=[
    path('',Home,name="home"),
    path('translate/',translate,name="translate")
]
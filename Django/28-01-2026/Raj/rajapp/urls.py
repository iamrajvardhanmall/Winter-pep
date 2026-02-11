from .views import RajView
from django.urls import path

urlpatterns = [
    path('', RajView),
]

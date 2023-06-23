from django.urls import path 
from . import api

urlpatterns= [
    path("", api.ReportAPI.as_view())
]

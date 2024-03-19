from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/<usrname>/', consumers.JoinAndLeave.as_asgi())
]  
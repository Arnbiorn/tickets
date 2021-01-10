from django.urls import path, include
from ticketsApp.views import *

urlpatterns = [
    path('event/', events.as_view()),
    path('ticket/', tickets.as_view()),
    path('availabletickets/', availableticketss.as_view()),
    path('userregistrationinfo/', userregistrationinfos.as_view()),
    path('usersessions/', usersessionss.as_view()),
    path('usertickets/', userticketss.as_view()),
]
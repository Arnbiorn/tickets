from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from ticketsApp.models import *
from ticketsApp.serializers import *

class events(APIView):
    """
    Event table api
    """

    def get(self, request):
        events = event.objects.all()
        serializer = eventSerializers(events, many=True)
        return Response(serializer.data.data)

class tickets(APIView):
    """
    Ticket table api
    """

    def get(self, request):
        tickets = ticket.objects.all()
        serializer = eventSerializers(tickets, many=True)
        return Response(serializer.data.data)

class availableticketss(APIView):
    """
    Available tickets table api
    """

    def get(self, request):
        availableticket = availabletickets.objects.all()
        serializer = eventSerializers(availableticket, many=True)
        return Response(serializer.data.data)

class userregistrationinfos(APIView):
    """
    User registration info table api
    """

    def get(self, request):
        userregistrationinfos = userregistrationinfo.objects.all()
        serializer = eventSerializers(userregistrationinfos, many=True)
        return Response(serializer.data.data)

class usersessionss(APIView):
    """
    User sessions table api
    """

    def get(self, request):
        usersession = usersessions.objects.all()
        serializer = eventSerializers(usersession, many=True)
        return Response(serializer.data.data)

class userticketss(APIView):
    """
    User tickets table api
    """

    def get(self, request):
        userticket = usertickets.objects.all()
        serializer = eventSerializers(userticket, many=True)
        return Response(serializer.data.data)


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

    permission_classes = [permissions.IsAuthenticated, ]
    #permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        events = event.objects.all()
        serializer = eventSerializers(events, many=True)
        return Response(serializer.data)

    def post(self, request):
        events = eventSerializers(data=request.data)
        if events.is_valid():
            events.save(data=request.data)
            return Response({"status": "Add"})
        else:
            return Response({"status": "Error"})

class tickets(APIView):

    """
    Ticket table api
    """

    permission_classes = [permissions.IsAuthenticated, ]
    #permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        tickets = ticket.objects.all()
        serializer = ticketSerializers(tickets, many=True)
        return Response(serializer.data)

    def post(self, request):
        tickets = eventSerializers(data=request.data)
        if tickets.is_valid():
            tickets.save(data=request.data)
            return Response({"status": "Add"})
        else:
            return Response({"status": "Error"})

class availableticketss(APIView):

    """
    Available tickets table api
    """

    permission_classes = [permissions.IsAuthenticated, ]
    #permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        availableticket = availabletickets.objects.all()
        serializer = availableticketsSerializers(availableticket, many=True)
        return Response(serializer.data)

    def post(self, request):
        availableticket = eventSerializers(data=request.data)
        if availableticket.is_valid():
            availableticket.save(data=request.data)
            return Response({"status": "Add"})
        else:
            return Response({"status": "Error"})

class userregistrationinfos(APIView):

    """
    User registration info table api
    """

    permission_classes = [permissions.IsAuthenticated, ]
    #permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        userregistrationinfos = userregistrationinfo.objects.all()
        serializer = userregistrationinfoSerializers(userregistrationinfos, many=True)
        return Response(serializer.data)

    def post(self, request):
        userregistrationinfos = eventSerializers(data=request.data)
        if userregistrationinfos.is_valid():
            userregistrationinfos.save(data=request.data)
            return Response({"status": "Add"})
        else:
            return Response({"status": "Error"})

class usersessionss(APIView):

    """
    User sessions table api
    """

    permission_classes = [permissions.IsAuthenticated, ]
    #permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        usersession = usersessions.objects.all()
        serializer = usersessionsSerializers(usersession, many=True)
        return Response(serializer.data)

    def post(self, request):
        usersession = eventSerializers(data=request.data)
        if usersession.is_valid():
            usersession.save(data=request.data)
            return Response({"status": "Add"})
        else:
            return Response({"status": "Error"})

class userticketss(APIView):

    """
    User tickets table api
    """

    permission_classes = [permissions.IsAuthenticated, ]
    #permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        userticket = usertickets.objects.all()
        serializer = userticketsSerializers(userticket, many=True)
        return Response(serializer.data)

    def post(self, request):
        userticket = eventSerializers(data=request.data)
        if userticket.is_valid():
            userticket.save(data=request.data)
            return Response({"status": "Add"})
        else:
            return Response({"status": "Error"})

from rest_framework import serializers

from ticketsApp.models import *

class eventSerializers(serializers.ModelSerializer):

    """
    Event model serializer
    """

    class Meta:
        model = event
        fields = (
            "description",
            "locationdescription",
            "latitude",
            "longitude",
            "name",
            "eventdate",
            "genre",
            "min_age",
            "imageid"
        )

class ticketSerializers(serializers.ModelSerializer):

    """
    Ticket model serializer
    """

    class Meta:
        model = ticket
        fields = (
            "id",
            "description",
            "name",
            "imageid",
            "event_id",
            "count",
            "price"
        )

class availableticketsSerializers(serializers.ModelSerializer):

    """
    Available tickets model serializer
    """

    class Meta:
        model = availabletickets
        fields = (
            "id",
            "available_count",
            "ticket_id"
        )

class userregistrationinfoSerializers(serializers.ModelSerializer):

    """
    User registration info model serializer
    """

    class Meta:
        model = userregistrationinfo
        fields = (
            "id",
            "email",
            "phone",
            "password",
            "user_role"
        )

class usersessionsSerializers(serializers.ModelSerializer):

    """
    User sessions model serializer
    """

    class Meta:
        model = usersessions
        fields = (
            "id",
            "user_id",
            "ticket_id",
            "opened_at",
            "status"
        )

class userticketsSerializers(serializers.ModelSerializer):

    """
    User tickets model serializer
    """

    class Meta:
        model = usertickets
        fields = (
            "user_tickets_id",
            "purchare_date",
            "user_id",
            "ticket_id"
        )
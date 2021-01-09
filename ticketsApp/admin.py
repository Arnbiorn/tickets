from django.contrib import admin
from ticketsApp.models import *

class eventAdmin(admin.ModelAdmin):

    """
    Event table admin panel
    """

    list_display = (
        "id",
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

class ticketAdmin(admin.ModelAdmin):

    """
    Ticket table admin panel
    """

    list_display = (
        "id",
        "description",
        "name",
        "imageid",
        "event_id",
        "count",
        "price"
    )

class availableticketsAdmin(admin.ModelAdmin):

    """
    Available tickets table admin panel
    """

    list_display = (
        "id",
        "available_count",
        "ticket_id"
    )

class userregistrationinfoAdmin(admin.ModelAdmin):

    """
    User registration info table admin panel
    """

    list_display = (
        "id",
        "email",
        "phone",
        "password",
        "user_role"
    )

class usersessionsAdmin(admin.ModelAdmin):

    """
    User sessions table admin panel
    """

    list_display = (
        "id",
        "user_id",
        "ticket_id",
        "opened_at",
        "status"
    )

class userticketsAdmin(admin.ModelAdmin):

    """
    User tickets table admin panel
    """

    list_display = (
        "user_tickets_id",
        "purchare_date",
        "user_id",
        "ticket_id"
    )


admin.site.register(event, eventAdmin)
admin.site.register(ticket, ticketAdmin)
admin.site.register(availabletickets, availableticketsAdmin)
admin.site.register(userregistrationinfo, userregistrationinfoAdmin)
admin.site.register(usersessions, usersessionsAdmin)
admin.site.register(usertickets, userticketsAdmin)

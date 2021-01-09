from django.db import models

from django.contrib.auth.models import User
# from djoser.urls.base import User

class event(models.Model):

    """
    This is model for events table
    """

    id = models.IntegerField(primary_key=True)
    description = models.TextField()
    locationdescription = models.TextField()
    latitude = models.DecimalField(max_digits=8, decimal_places=3)
    longitude = models.DecimalField(max_digits=8, decimal_places=3)
    name = models.TextField()
    eventdate = models.DateField(auto_now=False)
    genre = models.TextField()
    min_age = models.IntegerField()
    imageid = models.TextField()

    class Meta:
        verbose_name = "События"


class ticket(models.Model):

    """
    This is model for tickets table
    """

    id = models.IntegerField(primary_key=True)
    description = models.TextField()
    name = models.TextField()
    imageid = models.TextField()
    event_id = models.OneToOneField(event, on_delete=models.CASCADE)
    count = models.IntegerField()
    price = models.FloatField()

    class Meta:
        verbose_name = "Билеты"

class availabletickets(models.Model):

    """
    This is model for available tickets table
    """

    id = models.IntegerField(primary_key=True)
    available_count = models.IntegerField()
    ticket_id = models.OneToOneField(ticket, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Доступные билеты"

class userregistrationinfo(models.Model):

    """
    This is model for user registration info table
    """

    id = models.IntegerField(primary_key=True)
    email = models.EmailField()
    phone = models.TextField()
    password = models.CharField(max_length=50)
    user_role = models.TextField()

    class Meta:
        verbose_name = "Информация о полдьзователе"

class usersessions(models.Model):

    """
    This is model for user sessions table
    """

    id = models.IntegerField(primary_key=True)
    user_id = models.OneToOneField(userregistrationinfo, on_delete=models.CASCADE)
    ticket_id = models.OneToOneField(ticket, on_delete=models.CASCADE)
    opened_at = models.DateTimeField(auto_now=True, auto_created=True)
    status = models.BooleanField()

    class Meta:
        verbose_name = "Пользовательская сессия"

class usertickets(models.Model):

    """
    This is model for user tickets table
    """

    user_tickets_id = models.IntegerField(primary_key=True)
    purchare_date = models.DateField(auto_created=True, auto_now=True)
    user_id = models.OneToOneField(usersessions, on_delete=models.CASCADE)
    ticket_id = models.OneToOneField(ticket, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Пользовательский билет"
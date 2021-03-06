# Generated by Django 3.1.5 on 2021-01-09 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('locationdescription', models.TextField()),
                ('latitude', models.DecimalField(decimal_places=3, max_digits=8)),
                ('longitude', models.DecimalField(decimal_places=3, max_digits=8)),
                ('name', models.TextField()),
                ('eventdate', models.DateField()),
                ('genre', models.TextField()),
                ('min_age', models.IntegerField()),
                ('imageid', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'События',
                'verbose_name_plural': 'Cобытия',
            },
        ),
        migrations.CreateModel(
            name='ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('name', models.TextField()),
                ('imageid', models.TextField(blank=True, null=True)),
                ('event_id', models.IntegerField()),
                ('count', models.IntegerField()),
                ('price', models.FloatField()),
            ],
            options={
                'verbose_name': 'Билеты',
                'verbose_name_plural': 'Билеты',
            },
        ),
        migrations.CreateModel(
            name='userregistrationinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.TextField()),
                ('password', models.CharField(max_length=50)),
                ('user_role', models.TextField()),
            ],
            options={
                'verbose_name': 'Информация о полдьзователе',
                'verbose_name_plural': 'Информация о пользователе',
            },
        ),
        migrations.CreateModel(
            name='usertickets',
            fields=[
                ('purchare_date', models.DateField(auto_created=True, auto_now=True)),
                ('user_tickets_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('ticket_id', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Пользовательский билет',
                'verbose_name_plural': 'Пользовательский билет',
            },
        ),
        migrations.CreateModel(
            name='usersessions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opened_at', models.DateTimeField(auto_created=True, auto_now=True)),
                ('user_id', models.IntegerField()),
                ('status', models.BooleanField()),
                ('ticket_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ticketsApp.ticket')),
            ],
            options={
                'verbose_name': 'Пользовательская сессия',
                'verbose_name_plural': 'Пользовательская сессия',
            },
        ),
        migrations.CreateModel(
            name='availabletickets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available_count', models.IntegerField()),
                ('ticket_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ticketsApp.ticket')),
            ],
            options={
                'verbose_name': 'Доступные билеты',
                'verbose_name_plural': 'Доступные билеты',
            },
        ),
    ]

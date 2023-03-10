# Generated by Django 3.2 on 2023-03-07 02:02

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('civilité', models.CharField(choices=[('Mr', 'Mr'), ('Mme', 'Mme'), ('Mlle', 'Mlle')], default='Mr', max_length=150)),
                ('prénom', models.CharField(max_length=150)),
                ('nom_de_famille', models.CharField(max_length=100)),
                ('address_type', models.CharField(choices=[('S', 'Shipping')], max_length=1)),
                ('default', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('ordered_date', models.DateTimeField(blank=True, null=True)),
                ('ordered', models.BooleanField(default=False)),
                ('passenger_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='passenger_address', to='ticket.address')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depart', models.CharField(choices=[('Bunia', 'Bunia'), ('Kisangani', 'Kisangani'), ('Aru', 'Aru'), ('Mahagi', 'Mahagi'), ('Beni', 'Beni'), ('Goma', 'Goma')], default='New', max_length=150)),
                ('destination', models.CharField(choices=[('Bunia', 'Bunia'), ('Kisangani', 'Kisangani'), ('Aru', 'Aru'), ('Mahagi', 'Mahagi'), ('Beni', 'Beni'), ('Goma', 'Goma')], default='New', max_length=150)),
                ('date_du_vol', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('heure_du_vol', models.TimeField()),
                ('places_restantes', models.IntegerField()),
                ('prix_ticket', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='ticket.order')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket.ticket')),
            ],
        ),
    ]

# Generated by Django 5.1.7 on 2025-03-07 17:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserWaterIntake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_key', models.CharField(blank=True, max_length=500, null=True)),
                ('water_amount', models.FloatField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('email_frequency', models.IntegerField(choices=[(1, 'Every 1 hour'), (2, 'Every 2 hour'), (4, 'Every 4 hour'), (6, 'Every 6 hour'), (12, 'Every 12 hour'), (24, 'Every one day')])),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SaveGoal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complete', models.BooleanField(default=False)),
                ('points', models.PositiveIntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('water_intake', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='getdailydrink.userwaterintake')),
            ],
        ),
        migrations.CreateModel(
            name='WaterTake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cup', models.CharField(choices=[('250ml', '250ml'), ('500ml', '500ml'), ('1L', '1L')], max_length=100)),
                ('amount_liters', models.FloatField()),
                ('waterintake', models.FloatField(default=0.0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

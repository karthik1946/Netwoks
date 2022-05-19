# Generated by Django 4.0.4 on 2022-05-19 06:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('videochat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='privatevideochatroom',
            name='videouser1',
            field=models.ForeignKey(default='', editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='videouser1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='privatevideochatroom',
            name='videouser2',
            field=models.ForeignKey(default='', editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='videouser2', to=settings.AUTH_USER_MODEL),
        ),
    ]
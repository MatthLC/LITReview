# Generated by Django 4.0.2 on 2022-02-18 15:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_remove_user_follows'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='follows',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='follow'),
        ),
    ]

# Generated by Django 4.0.2 on 2022-03-02 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flux', '0006_remove_ticket_contributors_delete_ticketcontributor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='contributors',
        ),
        migrations.DeleteModel(
            name='ReviewContributor',
        ),
    ]

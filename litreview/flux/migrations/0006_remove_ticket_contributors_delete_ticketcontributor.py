# Generated by Django 4.0.2 on 2022-03-02 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flux', '0005_alter_review_rating_alter_review_ticket_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='contributors',
        ),
        migrations.DeleteModel(
            name='TicketContributor',
        ),
    ]
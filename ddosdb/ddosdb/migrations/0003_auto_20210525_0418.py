# Generated by Django 3.1 on 2021-05-25 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ddosdb', '0002_failedlogins'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FailedLogins',
            new_name='FailedLogin',
        ),
    ]

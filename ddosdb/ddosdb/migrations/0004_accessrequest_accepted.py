# Generated by Django 2.0.5 on 2018-06-08 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ddosdb', '0003_auto_20180523_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessrequest',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
    ]
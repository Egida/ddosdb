# Generated by Django 3.2.4 on 2021-07-27 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ddosdb', '0004_auto_20210525_0425'),
    ]

    operations = [
        migrations.AddField(
            model_name='remoteddosdb',
            name='pull',
            field=models.BooleanField(default=False, help_text='Sync from this DDoS-DB'),
        ),
        migrations.AddField(
            model_name='remoteddosdb',
            name='push',
            field=models.BooleanField(default=True, help_text='Sync towards this DDoS-DB'),
        ),
        migrations.AlterField(
            model_name='remoteddosdb',
            name='active',
            field=models.BooleanField(default=True, help_text='Activate to sync with this DDoS-DB'),
        ),
    ]
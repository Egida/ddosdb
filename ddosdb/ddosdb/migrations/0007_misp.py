# Generated by Django 3.2.12 on 2022-02-05 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ddosdb', '0006_auto_20210728_1712'),
    ]

    operations = [
        migrations.CreateModel(
            name='MISP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='A friendly name for the MISP instance', max_length=255, verbose_name='MISP name')),
                ('url', models.URLField(help_text='The base URL for the MISP', verbose_name='MISP URL')),
                ('authkey', models.CharField(help_text='Authentication key for the MISP Automation API', max_length=255, verbose_name='Authentication Key')),
                ('active', models.BooleanField(default=True, help_text='Check this to sync with this MISP')),
                ('push', models.BooleanField(default=False, help_text='Sync towards this MISP')),
                ('pull', models.BooleanField(default=True, help_text='Sync from this MISP')),
                ('check_cert', models.BooleanField(default=True, help_text='Whether to check remote certificate on https')),
            ],
            options={
                'verbose_name_plural': ' MISPs',
            },
        ),
    ]
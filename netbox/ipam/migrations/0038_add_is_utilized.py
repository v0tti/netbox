# Generated by Django 3.1 on 2020-09-24 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipam', '0037_ipaddress_assignment'),
    ]

    operations = [
        migrations.AddField(
            model_name='prefix',
            name='is_utilized',
            field=models.BooleanField(default=False),
        ),
    ]
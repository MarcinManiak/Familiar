# Generated by Django 3.0.3 on 2020-03-01 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logged', '0003_auto_20200301_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='who',
            field=models.CharField(default='None', max_length=256),
        ),
    ]

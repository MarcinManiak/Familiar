# Generated by Django 3.0.3 on 2020-03-02 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logged', '0010_auto_20200302_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
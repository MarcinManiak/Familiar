# Generated by Django 3.0.3 on 2020-03-16 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0006_auto_20200228_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='description',
            field=models.TextField(blank=True, help_text='Opcjonalne, ale na pewno czym szczególnym się odznaczacie :) '),
        ),
        migrations.AlterField(
            model_name='family',
            name='name',
            field=models.CharField(max_length=128),
        ),
    ]

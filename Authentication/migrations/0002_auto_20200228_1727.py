# Generated by Django 3.0.3 on 2020-02-28 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='family',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='family',
            name='name',
            field=models.CharField(help_text='Name your family', max_length=128),
        ),
    ]

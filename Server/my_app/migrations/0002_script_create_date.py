# Generated by Django 2.0.5 on 2018-10-21 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='script',
            name='create_date',
            field=models.DateField(default='2018-10-21'),
        ),
    ]

# Generated by Django 3.1.1 on 2020-10-18 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='', max_length=300),
        ),
    ]

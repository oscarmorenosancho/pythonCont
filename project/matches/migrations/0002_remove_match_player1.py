# Generated by Django 5.0.2 on 2024-03-11 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='player1',
        ),
    ]

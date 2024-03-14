# Generated by Django 5.0.2 on 2024-03-11 14:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0004_match_player2_alter_match_player1'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='player1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='match',
            name='player2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player2', to=settings.AUTH_USER_MODEL),
        ),
    ]

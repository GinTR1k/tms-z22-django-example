# Generated by Django 4.0.4 on 2022-05-16 16:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0002_alter_menuitem_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='priority',
            field=models.SmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(-100), django.core.validators.MaxValueValidator(100)]),
        ),
    ]

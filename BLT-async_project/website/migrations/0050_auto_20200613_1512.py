# Generated by Django 3.0.7 on 2020-06-13 15:12

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0049_auto_20200613_1429"),
    ]

    operations = [
        migrations.AddField(
            model_name="hunt",
            name="end_on",
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="hunt",
            name="starts_on",
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
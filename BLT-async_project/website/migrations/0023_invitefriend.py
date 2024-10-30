# Generated by Django 1.9.2 on 2016-12-28 20:13


import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("website", "0022_auto_20161212_1510"),
    ]

    operations = [
        migrations.CreateModel(
            name="InviteFriend",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("recipient", models.EmailField(max_length=254)),
                ("sent", models.DateTimeField(auto_now_add=True, db_index=True)),
                (
                    "sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
            options={
                "ordering": ("-sent",),
                "verbose_name": "invitation",
                "verbose_name_plural": "invitations",
            },
        ),
    ]
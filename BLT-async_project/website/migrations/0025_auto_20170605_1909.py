# Generated by Django 1.9.2 on 2017-06-05 19:09


import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models

import website.models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0024_userprofile"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("author", models.CharField(max_length=200)),
                ("author_url", models.CharField(max_length=200)),
                ("text", models.TextField()),
                ("created_date", models.DateTimeField(default=django.utils.timezone.now)),
                ("approved_comment", models.BooleanField(default=False)),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="website.Issue",
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="user_avatar",
            field=models.ImageField(
                blank=True, null=True, upload_to=website.models.user_images_path
            ),
        ),
    ]

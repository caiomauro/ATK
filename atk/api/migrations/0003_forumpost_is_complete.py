# Generated by Django 4.2.7 on 2023-11-04 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_forumpost_delete_userinfo"),
    ]

    operations = [
        migrations.AddField(
            model_name="forumpost",
            name="is_complete",
            field=models.BooleanField(default=False),
        ),
    ]

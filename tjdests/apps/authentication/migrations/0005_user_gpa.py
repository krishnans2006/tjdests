# Generated by Django 3.2 on 2021-04-22 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0004_auto_20210419_1713"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="GPA",
            field=models.FloatField(help_text="Weighted GPA", null=True),
        ),
    ]

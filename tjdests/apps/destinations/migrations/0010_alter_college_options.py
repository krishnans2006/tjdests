# Generated by Django 3.2 on 2021-04-23 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0009_alter_decision_admission_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='college',
            options={'ordering': ['name']},
        ),
    ]
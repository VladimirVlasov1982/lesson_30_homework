# Generated by Django 4.1.3 on 2022-11-28 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_user_managers"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="age",
            field=models.SmallIntegerField(null=True),
        ),
    ]

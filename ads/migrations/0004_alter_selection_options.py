# Generated by Django 4.1.3 on 2022-11-29 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0003_selection"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="selection",
            options={"verbose_name": "Подборка", "verbose_name_plural": "Подборки"},
        ),
    ]

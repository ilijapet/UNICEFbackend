# Generated by Django 4.2.7 on 2023-12-27 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_onetimepassword"),
    ]

    operations = [
        migrations.DeleteModel(name="OneTimePassword",),
    ]

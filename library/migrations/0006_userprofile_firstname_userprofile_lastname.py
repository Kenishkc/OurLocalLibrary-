# Generated by Django 4.2.3 on 2023-09-14 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0005_userprofile_address_userprofile_gender_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="firstname",
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="lastname",
            field=models.CharField(blank=True, max_length=10),
        ),
    ]

# Generated by Django 4.2.3 on 2023-09-14 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0006_userprofile_firstname_userprofile_lastname"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="email",
            field=models.CharField(blank=True, max_length=50),
        ),
    ]

# Generated by Django 4.2.3 on 2023-09-15 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0007_userprofile_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[("M", "Male"), ("F", "Female"), ("O", "Other")],
                max_length=10,
            ),
        ),
    ]
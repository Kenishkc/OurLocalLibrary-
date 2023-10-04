# Generated by Django 4.2.3 on 2023-10-04 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0009_borrowedbook"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="borrowedbook",
            name="book",
        ),
        migrations.AddField(
            model_name="borrowedbook",
            name="book_instance",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="library.bookinstance",
            ),
        ),
    ]
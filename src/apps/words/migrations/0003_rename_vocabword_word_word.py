# Generated by Django 4.2.3 on 2023-07-29 02:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("words", "0002_rename_word_word_vocabword"),
    ]

    operations = [
        migrations.RenameField(
            model_name="word",
            old_name="vocabWord",
            new_name="word",
        ),
    ]

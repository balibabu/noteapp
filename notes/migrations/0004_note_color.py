# Generated by Django 4.2.7 on 2023-11-28 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_alter_note_description_alter_note_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='color',
            field=models.CharField(default='rgb(220, 220, 220)', max_length=20),
        ),
    ]

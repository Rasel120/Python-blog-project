# Generated by Django 3.2.3 on 2021-05-26 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20210522_0959'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sliders',
            old_name='photo',
            new_name='image',
        ),
    ]
# Generated by Django 3.2.3 on 2021-05-27 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='datetime',
            field=models.DateTimeField(blank=True),
        ),
    ]

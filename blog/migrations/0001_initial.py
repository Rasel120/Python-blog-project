# Generated by Django 3.2.4 on 2021-06-16 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('datetime', models.DateTimeField(blank=True)),
                ('description', models.TextField(max_length=2000)),
            ],
        ),
    ]

# Generated by Django 3.1.2 on 2020-10-14 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstone_backend_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedasteroid',
            name='favorite',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='savedasteroid',
            name='note',
            field=models.TextField(blank=True),
        ),
    ]

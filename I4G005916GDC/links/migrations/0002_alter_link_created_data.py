# Generated by Django 4.0.5 on 2022-07-01 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='created_data',
            field=models.DateTimeField(),
        ),
    ]
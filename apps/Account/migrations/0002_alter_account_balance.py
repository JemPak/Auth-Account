# Generated by Django 3.2.9 on 2021-11-14 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='balance',
            field=models.BigIntegerField(default=0, verbose_name='Balance'),
        ),
    ]

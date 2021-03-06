# Generated by Django 3.2.9 on 2021-11-14 06:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id_account', models.BigAutoField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=30, verbose_name='City')),
                ('phone', models.BigIntegerField(verbose_name='Phone')),
                ('ages', models.IntegerField(verbose_name='Age')),
                ('register_date', models.DateField(auto_now_add=True, verbose_name='Register Date')),
                ('balance', models.BigIntegerField(verbose_name='Balance')),
                ('id_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

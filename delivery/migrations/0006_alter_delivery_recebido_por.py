# Generated by Django 4.0.6 on 2022-07-28 11:55

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('delivery', '0005_alter_delivery_data_entrada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='recebido_por',
            field=models.ForeignKey(default=django.contrib.auth.models.User, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

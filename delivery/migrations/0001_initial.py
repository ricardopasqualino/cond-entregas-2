# Generated by Django 4.0.6 on 2022-07-08 19:24

import delivery.models
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
            name='Box',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('box', models.CharField(default=None, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Casa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(default=None, max_length=3, null=True)),
                ('rua', models.CharField(default=None, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prestador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default=None, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefone', models.CharField(default=None, max_length=15, null=True)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Morador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default=None, max_length=200, null=True)),
                ('sobrenome', models.CharField(default=None, max_length=200, null=True)),
                ('telefone', models.CharField(default=None, max_length=40, null=True)),
                ('email', models.CharField(default=None, max_length=200, null=True)),
                ('casa', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='delivery.casa')),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(default=None, editable=False, max_length=10)),
                ('nota_fiscal', models.CharField(default=None, max_length=10)),
                ('data_entrada', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=False)),
                ('casa', models.ForeignKey(auto_created=True, default=delivery.models.Casa, on_delete=django.db.models.deletion.CASCADE, to='delivery.casa')),
                ('modulo', models.ForeignKey(auto_created=True, default=delivery.models.Box, on_delete=django.db.models.deletion.CASCADE, to='delivery.box')),
                ('recebido_por', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

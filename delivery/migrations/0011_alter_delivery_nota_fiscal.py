# Generated by Django 4.0.6 on 2022-09-27 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0010_morador_aceite_alertas_alter_delivery_casa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='nota_fiscal',
            field=models.DecimalField(decimal_places=6, default=None, max_digits=6),
        ),
    ]

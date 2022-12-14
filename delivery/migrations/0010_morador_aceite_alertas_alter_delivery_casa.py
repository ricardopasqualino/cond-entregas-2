# Generated by Django 4.0.6 on 2022-09-25 22:36

import delivery.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0009_alter_delivery_nota_fiscal'),
    ]

    operations = [
        migrations.AddField(
            model_name='morador',
            name='aceite_alertas',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='casa',
            field=models.ForeignKey(auto_created=True, default=delivery.models.Casa, on_delete=django.db.models.deletion.DO_NOTHING, to='delivery.casa'),
        ),
    ]

# Generated by Django 4.0.6 on 2022-08-18 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0007_delete_prestador_remove_morador_casa_casa_moradores_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casa',
            name='moradores',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='delivery.morador'),
        ),
    ]

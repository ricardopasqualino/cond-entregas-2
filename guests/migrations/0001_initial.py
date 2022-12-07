# Generated by Django 4.0.6 on 2022-09-02 00:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('delivery', '0008_alter_casa_moradores'),
    ]

    operations = [
        migrations.CreateModel(
            name='convidado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default=None, max_length=300, null=True)),
                ('documento', models.CharField(default=None, max_length=100, null=True)),
                ('veiculo', models.CharField(default=None, max_length=100, null=True)),
                ('autorizar_convidado', models.BooleanField(default=False)),
                ('anfitriao', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='delivery.morador')),
            ],
        ),
        migrations.CreateModel(
            name='evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_evento', models.DateTimeField(default=None)),
                ('qtd_convidados', models.CharField(default=None, max_length=100)),
                ('local_evento', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='visita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now=True)),
                ('convidado', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='guests.convidado')),
            ],
        ),
        migrations.CreateModel(
            name='lista_convidado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_lista', models.CharField(default=None, max_length=100)),
                ('convidados_lista', models.ManyToManyField(to='guests.convidado')),
            ],
        ),
    ]

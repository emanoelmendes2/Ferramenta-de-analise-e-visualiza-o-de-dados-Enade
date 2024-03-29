# Generated by Django 3.0.7 on 2021-07-01 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tdados', '0002_remove_dados_estado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kVizinhos', models.CharField(blank=True, max_length=16, null=True, unique=True)),
                ('dobrasF', models.CharField(blank=True, max_length=16, null=True, unique=True)),
                ('erro', models.CharField(blank=True, max_length=16, null=True, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='dados',
            name='resultado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Tdados.Resultado'),
        ),
    ]

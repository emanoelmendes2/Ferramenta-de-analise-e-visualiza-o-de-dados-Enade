# Generated by Django 3.0.7 on 2021-07-02 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tdados', '0003_auto_20210701_0150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dados',
            name='resultado',
        ),
        migrations.AddField(
            model_name='enade',
            name='resultado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Tdados.Resultado'),
        ),
    ]

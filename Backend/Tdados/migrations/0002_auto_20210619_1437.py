# Generated by Django 3.0.7 on 2021-06-19 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tdados', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estado',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]

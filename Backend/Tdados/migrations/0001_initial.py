# Generated by Django 3.0.7 on 2020-11-07 00:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.CharField(blank=True, max_length=16, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoInstituicao', models.IntegerField(blank=True, null=True)),
                ('orgAcademica', models.IntegerField(blank=True, null=True)),
                ('areaCurso', models.IntegerField(blank=True, null=True)),
                ('codigoCurso', models.IntegerField(blank=True, null=True)),
                ('modalidadeEnsino', models.IntegerField(blank=True, null=True)),
                ('municipioCurso', models.IntegerField(blank=True, null=True)),
                ('idade', models.IntegerField(blank=True, null=True)),
                ('sexo', models.CharField(blank=True, max_length=16, null=True)),
                ('anoFinalEM', models.IntegerField(blank=True, null=True)),
                ('iniciograd', models.IntegerField(blank=True, null=True)),
                ('turnoGrad', models.IntegerField(blank=True, null=True)),
                ('presencaenade', models.IntegerField(blank=True, null=True)),
                ('questao01', models.CharField(blank=True, max_length=16, null=True)),
                ('questao02', models.CharField(blank=True, max_length=16, null=True)),
                ('questao04', models.CharField(blank=True, max_length=16, null=True)),
                ('questao05', models.CharField(blank=True, max_length=16, null=True)),
                ('questao07', models.CharField(blank=True, max_length=16, null=True)),
                ('questao08', models.CharField(blank=True, max_length=16, null=True)),
                ('questao09', models.CharField(blank=True, max_length=16, null=True)),
                ('questao11', models.CharField(blank=True, max_length=16, null=True)),
                ('questao12', models.CharField(blank=True, max_length=16, null=True)),
                ('questao13', models.CharField(blank=True, max_length=16, null=True)),
                ('questao15', models.CharField(blank=True, max_length=16, null=True)),
                ('questao16', models.CharField(blank=True, max_length=16, null=True)),
                ('questao17', models.CharField(blank=True, max_length=16, null=True)),
                ('questao21', models.CharField(blank=True, max_length=16, null=True)),
                ('questao22', models.CharField(blank=True, max_length=16, null=True)),
                ('questao23', models.CharField(blank=True, max_length=16, null=True)),
                ('questao27', models.CharField(blank=True, max_length=16, null=True)),
                ('questao28', models.CharField(blank=True, max_length=16, null=True)),
                ('questao29', models.CharField(blank=True, max_length=16, null=True)),
                ('questao30', models.CharField(blank=True, max_length=16, null=True)),
                ('questao31', models.CharField(blank=True, max_length=16, null=True)),
                ('questao32', models.CharField(blank=True, max_length=16, null=True)),
                ('questao33', models.CharField(blank=True, max_length=16, null=True)),
                ('questao34', models.CharField(blank=True, max_length=16, null=True)),
                ('questao35', models.CharField(blank=True, max_length=16, null=True)),
                ('questao36', models.CharField(blank=True, max_length=16, null=True)),
                ('questao37', models.CharField(blank=True, max_length=16, null=True)),
                ('questao38', models.CharField(blank=True, max_length=16, null=True)),
                ('questao39', models.CharField(blank=True, max_length=16, null=True)),
                ('questao40', models.CharField(blank=True, max_length=16, null=True)),
                ('questao41', models.CharField(blank=True, max_length=16, null=True)),
                ('questao42', models.CharField(blank=True, max_length=16, null=True)),
                ('questao43', models.CharField(blank=True, max_length=16, null=True)),
                ('questao44', models.CharField(blank=True, max_length=16, null=True)),
                ('questao45', models.CharField(blank=True, max_length=16, null=True)),
                ('questao46', models.CharField(blank=True, max_length=16, null=True)),
                ('questao47', models.CharField(blank=True, max_length=16, null=True)),
                ('questao48', models.CharField(blank=True, max_length=16, null=True)),
                ('questao49', models.CharField(blank=True, max_length=16, null=True)),
                ('questao50', models.CharField(blank=True, max_length=16, null=True)),
                ('questao51', models.CharField(blank=True, max_length=16, null=True)),
                ('questao52', models.CharField(blank=True, max_length=16, null=True)),
                ('questao53', models.CharField(blank=True, max_length=16, null=True)),
                ('questao54', models.CharField(blank=True, max_length=16, null=True)),
                ('questao55', models.CharField(blank=True, max_length=16, null=True)),
                ('questao56', models.CharField(blank=True, max_length=16, null=True)),
                ('questao57', models.CharField(blank=True, max_length=16, null=True)),
                ('questao58', models.CharField(blank=True, max_length=16, null=True)),
                ('questao59', models.CharField(blank=True, max_length=16, null=True)),
                ('questao60', models.CharField(blank=True, max_length=16, null=True)),
                ('questao61', models.CharField(blank=True, max_length=16, null=True)),
                ('questao62', models.CharField(blank=True, max_length=16, null=True)),
                ('questao63', models.CharField(blank=True, max_length=16, null=True)),
                ('questao64', models.CharField(blank=True, max_length=16, null=True)),
                ('questao65', models.CharField(blank=True, max_length=16, null=True)),
                ('questao66', models.CharField(blank=True, max_length=16, null=True)),
                ('questao67', models.CharField(blank=True, max_length=16, null=True)),
                ('questao68', models.CharField(blank=True, max_length=16, null=True)),
                ('enade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Tdados.Enade')),
            ],
        ),
    ]

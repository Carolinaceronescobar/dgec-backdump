# Generated by Django 5.0 on 2023-12-13 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('haDictadoPrograma', models.CharField(max_length=200, null=True)),
                ('programaSeleccionado', models.CharField(max_length=200, null=True)),
                ('memoAdjunto', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]

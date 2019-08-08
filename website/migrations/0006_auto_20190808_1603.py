# Generated by Django 2.2.4 on 2019-08-08 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20190808_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='escola',
            name='codigo_acesso',
            field=models.CharField(error_messages={'unique': 'Código de acesso já existente.'}, max_length=12, unique=True, verbose_name='Registre um código de acesso'),
        ),
        migrations.AlterField(
            model_name='escola',
            name='email',
            field=models.EmailField(error_messages={'unique': 'Escola com este nome já está cadastrada em nosso sistema.'}, max_length=255, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='escola',
            name='nome_escola',
            field=models.CharField(error_messages={'unique': 'Escola com este nome já está cadastrada em nosso sistema.'}, max_length=255, unique=True, verbose_name='Nome da Escola'),
        ),
        migrations.AlterField(
            model_name='escola',
            name='senha_acesso',
            field=models.CharField(max_length=12, verbose_name='Registre uma senha de acesso'),
        ),
        migrations.AlterField(
            model_name='escola',
            name='telefone_escola',
            field=models.CharField(error_messages={'unique': 'Este número de telefone já existe. Verifique e tente novamente.'}, max_length=12, unique=True, verbose_name='Número de Telefone'),
        ),
    ]
# Generated by Django 2.2.4 on 2019-08-15 23:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_auto_20190815_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='escola',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.Escola'),
        ),
    ]

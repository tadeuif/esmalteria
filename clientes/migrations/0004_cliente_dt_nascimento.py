# Generated by Django 2.0 on 2019-08-25 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_auto_20190825_0258'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='dt_nascimento',
            field=models.DateField(default='1900-01-01'),
        ),
    ]

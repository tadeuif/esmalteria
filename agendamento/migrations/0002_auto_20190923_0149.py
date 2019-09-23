# Generated by Django 2.0 on 2019-09-23 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('dt_agendamento', models.DateField(default='1900-01-01')),
                ('hora_agendamento', models.TimeField(default='00:00:00')),
                ('servico_prestado', models.CharField(max_length=250)),
            ],
        ),
        migrations.DeleteModel(
            name='Produto',
        ),
    ]

# Generated by Django 4.0.5 on 2022-07-22 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sampletest',
            name='sampledate',
            field=models.DateField(),
        ),
        migrations.AlterModelTable(
            name='sampletest',
            table='Sampletest',
        ),
    ]

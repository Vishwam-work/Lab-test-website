# Generated by Django 4.0.5 on 2022-07-29 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0006_sampletest_gridradios'),
    ]

    operations = [
        migrations.AddField(
            model_name='sampletest',
            name='test1',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.0.5 on 2022-07-30 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0008_sampletest_test2'),
    ]

    operations = [
        migrations.AddField(
            model_name='sampletest',
            name='contename',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sampletest',
            name='in_gram',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]

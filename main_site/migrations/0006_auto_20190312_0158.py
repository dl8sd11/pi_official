# Generated by Django 2.1.7 on 2019-03-12 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0005_auto_20190312_0158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='response',
            field=models.TextField(blank=True, default=None),
        ),
    ]

# Generated by Django 2.1.7 on 2019-03-12 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0002_auto_20190312_0110'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='response',
            field=models.TextField(default=None),
        ),
    ]

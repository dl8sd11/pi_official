# Generated by Django 2.2.1 on 2019-05-24 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0016_remove_project_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='order',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

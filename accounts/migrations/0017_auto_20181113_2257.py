# Generated by Django 2.1.2 on 2018-11-13 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_post_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]

# Generated by Django 2.1.2 on 2018-11-12 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20181112_0033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.AlterField(
            model_name='post',
            name='post',
            field=models.CharField(default='', max_length=100),
        ),
    ]

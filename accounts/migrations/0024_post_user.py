# Generated by Django 2.1.2 on 2018-11-14 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_remove_post_luser'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.CharField(default='', max_length=100),
        ),
    ]

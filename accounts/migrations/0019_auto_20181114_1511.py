# Generated by Django 2.1.2 on 2018-11-14 15:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0018_post_person'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='person',
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

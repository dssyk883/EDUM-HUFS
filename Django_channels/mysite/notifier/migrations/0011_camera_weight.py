# Generated by Django 2.1.3 on 2018-12-04 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifier', '0010_camera_fence'),
    ]

    operations = [
        migrations.AddField(
            model_name='camera',
            name='weight',
            field=models.IntegerField(default=1),
        ),
    ]

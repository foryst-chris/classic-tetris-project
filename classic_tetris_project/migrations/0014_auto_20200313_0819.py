# Generated by Django 2.2.4 on 2020-03-13 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classic_tetris_project', '0013_delete_coin'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ntsc_pb_19',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='ntsc_pb_19_updated_at',
            field=models.DateTimeField(null=True),
        ),
    ]
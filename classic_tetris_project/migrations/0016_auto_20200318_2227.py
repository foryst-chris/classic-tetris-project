# Generated by Django 2.2.4 on 2020-03-18 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classic_tetris_project', '0015_auto_20200318_0315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customcommand',
            name='alias_for',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classic_tetris_project.CustomCommand'),
        ),
        migrations.AlterField(
            model_name='customcommand',
            name='output',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
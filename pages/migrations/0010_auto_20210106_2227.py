# Generated by Django 3.1.3 on 2021-01-06 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_auto_20210106_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='Geo_Type',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='board_n101',
            name='Geo_Type',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='board_n103',
            name='Geo_Type',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='board_n106',
            name='Geo_Type',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='board_n109',
            name='Geo_Type',
            field=models.CharField(max_length=20),
        ),
    ]

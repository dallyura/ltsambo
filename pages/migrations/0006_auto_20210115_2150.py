# Generated by Django 3.1.3 on 2021-01-15 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20210115_0708'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='Tooth_Qty',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='board_n101',
            name='Tooth_Qty',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='board_n103',
            name='Tooth_Qty',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='board_n106',
            name='Tooth_Qty',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='board_n109',
            name='Tooth_Qty',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='board_t316',
            name='Tooth_Qty',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
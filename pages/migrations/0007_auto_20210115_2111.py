# Generated by Django 3.1.3 on 2021-01-15 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20210115_2102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='Tooth_Qty',
        ),
        migrations.RemoveField(
            model_name='board_n101',
            name='Tooth_Qty',
        ),
        migrations.RemoveField(
            model_name='board_n103',
            name='Tooth_Qty',
        ),
        migrations.RemoveField(
            model_name='board_n106',
            name='Tooth_Qty',
        ),
        migrations.RemoveField(
            model_name='board_n109',
            name='Tooth_Qty',
        ),
        migrations.RemoveField(
            model_name='board_t316',
            name='Tooth_Qty',
        ),
    ]
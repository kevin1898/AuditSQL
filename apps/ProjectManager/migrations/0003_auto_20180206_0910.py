# Generated by Django 2.0.2 on 2018-02-06 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectManager', '0002_auto_20180205_1728'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='remark',
            options={'default_permissions': (), 'verbose_name': '线上审计备注表', 'verbose_name_plural': '线上审计备注表'},
        ),
    ]

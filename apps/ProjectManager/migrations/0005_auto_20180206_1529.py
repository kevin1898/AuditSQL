# Generated by Django 2.0.2 on 2018-02-06 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectManager', '0004_auto_20180206_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='onlineauditcontents',
            name='fact_operate_dba',
            field=models.CharField(default='', max_length=30, verbose_name='实际执行dba'),
        ),
        migrations.AddField(
            model_name='onlineauditcontents',
            name='fact_verifier',
            field=models.CharField(default='', max_length=30, verbose_name='实际审批人'),
        ),
        migrations.AlterField(
            model_name='onlineauditcontents',
            name='close_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='关闭时间'),
        ),
    ]

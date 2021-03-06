# Generated by Django 2.0.2 on 2018-02-06 14:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectManager', '0003_auto_20180206_0910'),
    ]

    operations = [
        migrations.AddField(
            model_name='onlineauditcontents',
            name='close_reason',
            field=models.CharField(default='', max_length=1024, verbose_name='关闭原因'),
        ),
        migrations.AddField(
            model_name='onlineauditcontents',
            name='close_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='记录关闭时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='onlineauditcontents',
            name='close_user',
            field=models.CharField(default='', max_length=30, verbose_name='关闭记录的用户'),
        ),
        migrations.AddField(
            model_name='onlineauditcontents',
            name='operate_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='DBA处理的时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='onlineauditcontents',
            name='verifier_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='leader审批时间'),
            preserve_default=False,
        ),
    ]

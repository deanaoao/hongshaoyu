# Generated by Django 2.2.6 on 2019-10-08 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useradmin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='telephone',
            field=models.IntegerField(blank=True, null=True, unique=True, verbose_name='手机号码'),
        ),
    ]
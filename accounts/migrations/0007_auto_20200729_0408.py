# Generated by Django 3.0.8 on 2020-07-28 19:08

import annoying.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200729_0334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='interrest_tag1',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='interrest_tag2',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='interrest_tag3',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='second_viliage',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='third_viliage',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='user',
            field=annoying.fields.AutoOneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

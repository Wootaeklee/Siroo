# Generated by Django 3.0.8 on 2020-07-29 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_vil'),
    ]

    operations = [
        migrations.AddField(
            model_name='vil',
            name='vil',
            field=models.CharField(max_length=10, null=True),
        ),
    ]

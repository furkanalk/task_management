# Generated by Django 4.1.7 on 2023-08-07 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(default='idle', max_length=50),
        ),
    ]

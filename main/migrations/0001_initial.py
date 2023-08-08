# Generated by Django 4.1.7 on 2023-08-07 14:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=50)),
                ('task_description', models.TextField(max_length=200)),
                ('due_date', models.TextField(max_length=30)),
                ('assignee_name', models.TextField(blank=True, max_length=20)),
                ('status', models.CharField(choices=[('idle', 'idle'), ('to Do', 'to Do'), ('in Progress', 'in Progress'), ('Done', ' Done')], default='idle', max_length=15)),
                ('assignee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Tasks',
                'ordering': ('-status',),
            },
        ),
    ]
# Generated by Django 3.2 on 2022-08-08 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0015_alter_status_unique_together'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Status',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
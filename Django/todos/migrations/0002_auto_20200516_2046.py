# Generated by Django 3.0.6 on 2020-05-16 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='kind',
            new_name='action',
        ),
    ]
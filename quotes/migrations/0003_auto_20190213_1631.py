# Generated by Django 2.0.8 on 2019-02-14 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0002_auto_20190212_1437'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote',
            old_name='title',
            new_name='attribution',
        ),
        migrations.RenameField(
            model_name='quote',
            old_name='text',
            new_name='quote_text',
        ),
    ]
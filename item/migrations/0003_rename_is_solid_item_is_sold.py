# Generated by Django 5.0.2 on 2024-02-10 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_category_options_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='is_solid',
            new_name='is_sold',
        ),
    ]
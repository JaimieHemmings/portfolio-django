# Generated by Django 4.2 on 2024-10-09 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0005_rename_description_portfolioitem_description_one_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolioitem',
            old_name='description_teo',
            new_name='description_two',
        ),
    ]

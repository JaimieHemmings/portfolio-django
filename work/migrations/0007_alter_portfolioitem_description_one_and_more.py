# Generated by Django 4.2 on 2024-10-22 13:35

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0006_rename_description_teo_portfolioitem_description_two'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolioitem',
            name='description_one',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='portfolioitem',
            name='description_two',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
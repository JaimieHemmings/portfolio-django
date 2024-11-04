# Generated by Django 4.2 on 2024-10-22 13:36

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_blog_second_content_alter_blog_first_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='second_content',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='third_content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
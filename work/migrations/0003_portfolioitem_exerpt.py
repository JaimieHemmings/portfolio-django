# Generated by Django 4.2 on 2024-10-09 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0002_portfolioitem_external_link_portfolioitem_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolioitem',
            name='exerpt',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]

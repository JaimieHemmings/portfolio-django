# Generated by Django 4.2 on 2024-10-09 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('business_info', models.TextField()),
                ('target_audience', models.TextField()),
                ('usp', models.TextField()),
                ('leads', models.TextField()),
                ('branding', models.TextField()),
                ('budget', models.CharField(max_length=100)),
                ('completion_date', models.DateField()),
                ('additional_info', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
# Generated by Django 4.1.3 on 2023-05-09 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_settings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetting',
            name='about_us',
            field=models.TextField(blank=True, null=True, verbose_name='درباره ی ما'),
        ),
    ]
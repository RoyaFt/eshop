# Generated by Django 4.1.3 on 2023-04-02 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_sliders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slider',
            options={'verbose_name': 'اسلایدر', 'verbose_name_plural': 'اسلایدر ها'},
        ),
        migrations.RemoveField(
            model_name='slider',
            name='link',
        ),
    ]

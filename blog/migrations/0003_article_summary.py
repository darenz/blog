# Generated by Django 2.1.5 on 2019-01-31 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190130_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='summary',
            field=models.TextField(blank=True),
        ),
    ]

# Generated by Django 4.2.1 on 2023-07-15 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseteacher',
            name='about',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]

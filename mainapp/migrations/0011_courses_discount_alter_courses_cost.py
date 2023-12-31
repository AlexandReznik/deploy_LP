# Generated by Django 4.2.1 on 2023-07-09 09:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_remove_category_courses_courses_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='discount',
            field=models.IntegerField(blank=True, default=None, null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='courses',
            name='cost',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

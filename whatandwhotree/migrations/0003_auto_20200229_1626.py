# Generated by Django 3.0.3 on 2020-02-29 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whatandwhotree', '0002_auto_20200229_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='term',
            name='text',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='type',
            name='text',
            field=models.TextField(blank=True, default=''),
        ),
    ]

# Generated by Django 4.0.1 on 2022-01-17 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_coffee_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffee_stock',
            name='tasting_notes',
            field=models.TextField(max_length=200),
        ),
    ]

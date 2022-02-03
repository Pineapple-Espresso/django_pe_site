# Generated by Django 4.0.1 on 2022-01-17 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='coffee_stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin_city', models.CharField(max_length=25)),
                ('origin_country', models.CharField(max_length=25)),
                ('varietal', models.CharField(max_length=25)),
                ('process', models.CharField(max_length=25)),
                ('tasting_notes', models.CharField(max_length=25)),
                ('current_stock', models.IntegerField()),
            ],
        ),
    ]
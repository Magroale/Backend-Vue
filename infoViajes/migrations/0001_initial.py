# Generated by Django 4.1.13 on 2023-11-15 22:04

import django.core.validators
from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('text_Comments', models.TextField(max_length=2000)),
                ('personName', models.CharField(max_length=2000)),
            ],
            options={
                'db_table': 'Comentarios',
            },
        ),
        migrations.CreateModel(
            name='Viaje',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('country', models.CharField(max_length=2000)),
                ('location', models.CharField(max_length=200)),
                ('score', models.DecimalField(decimal_places=1, max_digits=2, validators=[django.core.validators.MinValueValidator(limit_value=0), django.core.validators.MaxValueValidator(limit_value=5)])),
                ('discount', models.BooleanField(default=False)),
                ('discountPercentage', models.DecimalField(decimal_places=2, max_digits=2, validators=[django.core.validators.MinValueValidator(limit_value=0), django.core.validators.MaxValueValidator(limit_value=1)])),
                ('price', models.IntegerField()),
                ('numberDays', models.IntegerField(validators=[django.core.validators.MaxValueValidator(limit_value=30)])),
                ('news', models.TextField(max_length=2000)),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
                'db_table': 'Viajes',
            },
        ),
    ]

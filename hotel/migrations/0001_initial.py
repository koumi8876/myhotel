# Generated by Django 4.2.7 on 2023-12-02 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=15)),
                ('hotel_country', models.CharField(max_length=15)),
                ('hotel_city', models.CharField(max_length=10)),
                ('hotel_email', models.CharField(max_length=20)),
                ('hotel_address', models.CharField(max_length=15)),
            ],
        ),
    ]

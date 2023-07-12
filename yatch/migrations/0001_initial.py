# Generated by Django 3.1 on 2023-07-07 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='D:\\python\\web_scraping\\django\\demo\\static\\img')),
                ('description', models.CharField(max_length=300)),
                ('offer', models.BooleanField()),
            ],
        ),
    ]

# Generated by Django 3.0.8 on 2020-07-19 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qiyou', '0008_user_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='city_route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=20)),
                ('route_name', models.CharField(max_length=100)),
                ('distance', models.CharField(max_length=20)),
                ('path', models.CharField(max_length=500)),
                ('link', models.CharField(max_length=100)),
                ('route_landscape', models.CharField(max_length=100)),
            ],
        ),
    ]

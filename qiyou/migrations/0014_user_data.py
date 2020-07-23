# Generated by Django 3.0.8 on 2020-07-20 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qiyou', '0013_delete_user_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('path', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=20)),
                ('route', models.TextField()),
                ('save', models.CharField(max_length=20)),
            ],
        ),
    ]

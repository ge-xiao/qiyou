# Generated by Django 3.0.8 on 2020-07-20 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qiyou', '0020_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='category',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='path',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='route',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='save',
            field=models.CharField(max_length=20, null=True),
        ),
    ]

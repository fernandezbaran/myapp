# Generated by Django 3.2.19 on 2024-08-18 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20240818_0535'),
    ]

    operations = [
        migrations.AddField(
            model_name='formresponse',
            name='dni',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='formresponse',
            name='motivo',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='formresponse',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

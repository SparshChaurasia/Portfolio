# Generated by Django 3.2.9 on 2022-06-22 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='Name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

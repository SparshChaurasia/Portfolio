# Generated by Django 3.2.9 on 2022-06-22 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20220622_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='Email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='contact',
            name='Name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
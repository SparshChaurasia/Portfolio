# Generated by Django 3.2.9 on 2022-06-22 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_contact_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='Email',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='contact',
            name='Name',
            field=models.CharField(max_length=60, null=True),
        ),
    ]

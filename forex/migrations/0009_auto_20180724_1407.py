# Generated by Django 2.0.1 on 2018-07-24 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forex', '0008_remove_register_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='email',
            field=models.CharField(max_length=20),
        ),
    ]
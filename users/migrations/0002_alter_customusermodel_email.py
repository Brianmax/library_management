# Generated by Django 4.2.1 on 2023-05-27 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusermodel',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
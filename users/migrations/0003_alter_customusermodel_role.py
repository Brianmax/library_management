# Generated by Django 4.2.1 on 2023-05-29 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customusermodel_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusermodel',
            name='role',
            field=models.CharField(choices=[(1, 'student'), (2, 'teacher'), (3, 'admin')], default='student', max_length=10),
        ),
    ]

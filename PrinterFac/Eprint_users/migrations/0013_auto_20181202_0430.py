# Generated by Django 2.1.3 on 2018-12-01 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eprint_users', '0012_auto_20181202_0349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.png', upload_to='profilepics'),
        ),
    ]

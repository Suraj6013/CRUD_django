# Generated by Django 5.0.6 on 2024-07-17 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='username',
        ),
        migrations.AlterField(
            model_name='login',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]

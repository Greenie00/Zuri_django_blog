# Generated by Django 4.0.5 on 2022-06-17 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.TextField(max_length=200),
        ),
    ]

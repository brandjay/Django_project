# Generated by Django 3.2.12 on 2022-05-26 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_rename_posts_user_posts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_posts',
            name='quote',
            field=models.TextField(),
        ),
    ]

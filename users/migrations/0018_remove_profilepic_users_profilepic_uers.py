# Generated by Django 4.0.2 on 2022-10-10 08:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0017_rename_user_profilepic_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilepic',
            name='Users',
        ),
        migrations.AddField(
            model_name='profilepic',
            name='uers',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
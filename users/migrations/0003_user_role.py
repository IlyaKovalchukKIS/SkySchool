# Generated by Django 4.2.5 on 2023-10-10 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_username_user_avatar_user_country_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('member', 'member'), ('manager', 'manager')], max_length=10, null=True),
        ),
    ]
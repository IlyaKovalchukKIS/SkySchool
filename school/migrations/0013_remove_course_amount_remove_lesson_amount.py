# Generated by Django 4.2.5 on 2023-10-21 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0012_alter_lesson_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='amount',
        ),
    ]
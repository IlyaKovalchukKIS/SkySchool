# Generated by Django 4.2.5 on 2023-10-21 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0010_alter_payment_date_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='amount',
            field=models.IntegerField(default=1, verbose_name='стоимость'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='amount',
            field=models.IntegerField(default=1, verbose_name='стоимость'),
        ),
    ]

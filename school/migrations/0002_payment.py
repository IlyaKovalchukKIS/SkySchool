# Generated by Django 4.2.5 on 2023-10-03 20:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_payment', models.DateTimeField(verbose_name='дата платежа')),
                ('payment_amount', models.PositiveIntegerField(verbose_name='сумма оплаты')),
                ('payment_method', models.CharField(choices=[('card', 'карта'), ('cash', 'наличные')], max_length=30, verbose_name='способ оплаты')),
                ('course_payment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school.course', verbose_name='курс')),
                ('lesson_payment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school.lesson', verbose_name='урок')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'оплата',
                'verbose_name_plural': 'оплаты',
                'ordering': ('-date_payment',),
            },
        ),
    ]

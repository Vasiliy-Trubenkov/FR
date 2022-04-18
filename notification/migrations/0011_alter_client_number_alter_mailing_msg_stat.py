# Generated by Django 4.0.2 on 2022-04-12 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0010_alter_mailing_msg_stat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='number',
            field=models.DecimalField(decimal_places=0, max_digits=11, unique=True, verbose_name='Номер телефона 7XXXXXXXXXX'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='msg_stat',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=7, verbose_name='Количество отправленных сообщений'),
        ),
    ]
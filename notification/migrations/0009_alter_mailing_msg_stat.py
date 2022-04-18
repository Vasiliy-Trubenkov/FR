# Generated by Django 4.0.2 on 2022-04-10 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0008_mailing_msg_stat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='msg_stat',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=7, verbose_name='Количество отправленных сообщений'),
        ),
    ]
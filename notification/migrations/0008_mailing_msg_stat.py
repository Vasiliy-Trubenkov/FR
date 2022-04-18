# Generated by Django 4.0.2 on 2022-04-10 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0007_mailing_theme'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailing',
            name='msg_stat',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=7, verbose_name='Количество отправленных сообщений'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.0.2 on 2022-04-10 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0006_mailing_foperator_mailing_ftag'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailing',
            name='theme',
            field=models.CharField(default='', max_length=30, verbose_name='Тема рассылки'),
        ),
    ]
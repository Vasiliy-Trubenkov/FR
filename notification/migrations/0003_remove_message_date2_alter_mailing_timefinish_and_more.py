# Generated by Django 4.0.2 on 2022-04-08 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0002_mailing_alter_client_options_remove_client_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='date2',
        ),
        migrations.AlterField(
            model_name='mailing',
            name='timefinish',
            field=models.DateTimeField(verbose_name='Время окончания рассылки'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='timestart',
            field=models.DateTimeField(verbose_name='Время начала рассылки'),
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(verbose_name='Дата создания сообщения'),
        ),
    ]
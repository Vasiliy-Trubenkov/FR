from django.db import models

# Create your models here.
class Mailing(models.Model):
    # Рассылка
    theme = models.CharField('Тема рассылки', max_length=30, default='')
    text = models.TextField('Содержание рассылки', max_length=1000)
    timestart = models.DateTimeField("Время начала рассылки")
    timefinish = models.DateTimeField("Время окончания рассылки")
    ftag = models.CharField('Тег клиента', max_length=30, blank=True)
    foperator = models.DecimalField('Код мобильного оператора', max_digits=3, decimal_places=0)
    msg_stat = models.DecimalField('Количество отправленных сообщений', max_digits=7, decimal_places=0,default=0, blank=True)
    # user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE) # каскадное удаление
    # после добавления сообщения возвращаемся сюда:
    def get_absolute_url(self):
        return 'home'

    def __str__(self):
        return self.theme  # для красивого отображения надписей (названий) на экране

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class Client(models.Model):
    name = models.CharField(verbose_name='Имя (необязательно)', max_length=50, default='', blank=True)
    number = models.DecimalField('Номер телефона 7XXXXXXXXXX', max_digits=11, decimal_places=0, unique=True)
    operator = models.DecimalField('Код мобильного оператора', max_digits=3, decimal_places=0)
    tag = models.CharField('Тег', max_length=30, blank=True)
    timezone = models.DecimalField('Часовой пояс клиента', max_digits=3, decimal_places=0, default='')

    # проверка корректности заполнения номера
    def clean(self):
        if len(str(self.number)) == 10 and str(self.number)[0] == '9':
            self.number += 70000000000

    # после добавления клиента возвращаемся сюда:
    def get_absolute_url(self):
        return 'directory'


    def __str__(self):
        return str(self.number)   # для красивого отображения надписей (названий) на экране

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Message(models.Model):
    date = models.DateTimeField("Дата создания сообщения", auto_now_add=True)
    status = models.CharField("Статус отправки", max_length=10) # Отправлено , В очереди , Не отправлено
    mailing_list_id = models.DecimalField("id рассылки", max_digits=7, decimal_places=0)
    client_id = models.DecimalField("id клиента", max_digits=7, decimal_places=0)

    # после добавления сообщения возвращаемся сюда:
    def get_absolute_url(self):
        return 'home'

    def __str__(self):
        return str(self.id)  # для красивого отображения надписей (названий) на экране

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

# Сервис уведомлений
## Тестовое задание для Фабрики Решений

## Содержание
* [Введение](#Введение)
* [Технологии](#Технологии)
* [Функции](#Функции)
* [Установка](#Установка)
* [Контакты](#Контакты)

## Введение
Данный проект является тестовым заданием для Фабрики Решений и представляет собой написанный на Джанго сервис рассылки уведомлений.
Все управление сервисом происходит через интерфейс написанного для данного сервиса сайта.

## Технологии
* Python 3.10.2
* HTML
* CSS
* Django 4.0.2
* Schedule 1.1.0

## Функции
* Добавление нового клиента в справочник со всеми его атрибутами
* Обновление данных атрибутов клиента
* Удаление клиента из справочника
* Добавление новой рассылки со всеми её атрибутами
* Получение общей статистики по созданным рассылкам и количеству отправленных сообщений по ним с группировкой по статусам
* Получение детальной статистики отправленных сообщений по конкретной рассылке
* Обновление атрибутов рассылки
* Удаление рассылки
* Обработка активных рассылок и отправка сообщений клиентам
* Поллинг выполнен с использованием модуля Schedule 1.1.0
* Все функции представлены понятным графическим интерфейсом, написанным на Django

## Установка
Для запуска сервиса выполните команду в директории проекта
```
python manage.py runserver
```
Сайт запустится на локальном порте в режиме отладки.

# Контакты
Проект разработан Василием Трубенковым
vasiliy.trubenkov@gmail.com
Екатеринбург 2022
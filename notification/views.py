from django.shortcuts import render, redirect
from .forms import ClientForm, MailingForm
from .models import Client, Mailing, Message
from django.views.generic import UpdateView, DeleteView, DetailView
from datetime import datetime, timezone, timedelta


# Create your views here.

def home(request):
    return render(request, 'notification/index.html')


def create_client(request):
    error = ''
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('directory')
        else:
            error = 'Форма заполнена неверно'

    form = ClientForm
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'notification/create_client.html', data)


class ClientUpdateView(UpdateView):
    model = Client
    template_name = 'notification/create_client.html'
    context_object_name = 'client_key_url'
    form_class = ClientForm
    success_url = '/directory'


class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'notification/delete_client.html'
    context_object_name = 'client_key_url'
    success_url = '/directory'


def create_mailing(request):
    error = ''
    if request.method == 'POST':
        form = MailingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена неверно'

    form = MailingForm
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'notification/create_mailing.html', data)

class MailingUpdateView(UpdateView):
    model = Mailing
    template_name = 'notification/create_mailing.html'
    context_object_name = 'mailing_key_url'
    form_class = MailingForm
    success_url = '/mailing_statistic'


class MailingDetailView(DetailView):
    model = Mailing
    template_name = 'notification/mailing_more.html'
    context_object_name = 'mailing_key_url'
    success_url = '/mailing_statistic'
    @staticmethod
    def all_messages():
        return Message.objects.all()


class MailingDeleteView(DeleteView):
    model = Mailing
    template_name = 'notification/delete_mailing.html'
    context_object_name = 'mailing_key_url'
    success_url = '/mailing_statistic'


def directory(request):
    client_view = Client.objects.order_by('id')
    return render(request, 'notification/directory.html',{'client_view': client_view})


def mailing_statistic(request):
    mailing_view = Mailing.objects.order_by('id')
    count = Mailing.objects.count()
    return render(request, 'notification/mailing_statistic.html', {'mailing_view': mailing_view, 'count':count})


def mailing_check():
    # вычисляем текущее время клиента по полю timezone:
    # текущее время клиента (ТВК) = текущее время UTC + часовой пояс клиента
    # если ТВК больше/равно времени рассылки и меньше времени окончания рассылки;
    # если тэг и оператор клиента совпадают с тегом и оператором рассылки;
    # если во всех сообщениях нет такого сообщения, в котором есть тэги клиента и рассылки
    # (то есть сообщения клиенту в ходе данной рассылки не отправлялось), то отправляем сообщение по данной рассылке
    for client in Client.objects.all():
        for mailing in Mailing.objects.all():
            client_current_time = datetime.now(timezone.utc) + timedelta(hours=int(client.timezone))
            if client_current_time >= mailing.timestart:
                if client_current_time < mailing.timefinish:
                    if client.tag == mailing.ftag and client.operator == mailing.foperator:
                        message_exist = False
                        for message in Message.objects.all():
                            if int(message.client_id) == int(client.id) and int(message.mailing_list_id) == int(mailing.id) and message.status == 'Отправлено':
                                message_exist = True
                        if message_exist == False:
                            do_request(client=client, mailing=mailing)
    return True

def update_mailing_status_msg():
    for mailing in Mailing.objects.all():
        msg_count = 0
        for message in Message.objects.all():
            if mailing.id == message.mailing_list_id:
                msg_count += 1
        Mailing.objects.filter(id=mailing.id).update(msg_stat=msg_count)

import requests
import json
def do_request(client, mailing):
    obj, created = Message.objects.update_or_create(
        mailing_list_id=str(mailing.id), client_id=str(client.id), status='Не отправлено', date=datetime.now(timezone.utc))
    jwt = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODE1NTczMjQsImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6IlZhc2lsaXlUcnViZW5rb3YifQ.JhiQto2K7Z5_C11sOthxALN-gIuaZgPivz8wxYuCI7M'
    url = "https://probe.fbrq.cloud/v1/send/" + str(obj.id)
    headers = {"accept": "application/json", 'Authorization': jwt, "Content-Type": "application/json"}
    data = {'id': obj.id, 'phone': int(client.number), 'text': str(mailing.text)}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    if r.json()['message'] == 'OK':
        Message.objects.filter(id=obj.id).update(status='Отправлено')
        update_mailing_status_msg()

# Поллинг
import schedule
from time import sleep
from threading import Thread

def scheduler():
    schedule.every(10).seconds.do(mailing_check)

    while False:
        schedule.run_pending()
        sleep(1)  # Выберите оптимальное значение под свои задачи планировщика


# Создаём и запускаем планировщик в отдельном потоке
t = Thread(target=scheduler).start()
from .models import Client, Mailing, Message
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, NumberInput
import datetime

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['number', 'name', 'operator', 'tag', 'timezone']
        widgets = {
            'name':TextInput(attrs={
                'placeholder':"Имя (необязательно)",
                'class':"form-control"
            }),
            'number': NumberInput(attrs={
                'placeholder': "Номер телефона 7XXXXXXXXXX",
                'class': "form-control",
            }),
            'operator': NumberInput(attrs={
                'placeholder': "Код оператора",
                'class': "form-control"
            }),
            'tag': TextInput(attrs={
                'placeholder': "Тег",
                'class': "form-control"
            }),
            'timezone': NumberInput(attrs={
                'placeholder': "Часовой пояс",
                'class': "form-control"
            }),
        }


class MailingForm(ModelForm):
    class Meta:
        model = Mailing
        fields = ['theme', 'text', 'timestart', 'timefinish', 'ftag', 'foperator']
        widgets = {
            'theme':TextInput(attrs={
                'placeholder': "Тема рассылки",
                'class': 'form-control'
            }),
            'text': Textarea(attrs={
                'placeholder': "Текст рассылки",
                'class': "form-control"
            }),
            'timestart': DateTimeInput(attrs={
                'class': "form-control",
                'placeholder':'Дата начала рассылки',
                'value': str(datetime.datetime.now())[:-7]
            }),
            'timefinish': DateTimeInput(attrs={
                'class': "form-control",
                'placeholder':'Дата окончания рассылки',
                'value': str(datetime.datetime.now())[:-7]
            }),
            'foperator': NumberInput(attrs={
                'placeholder': "Код оператора",
                'class': "form-control"
            }),
            'ftag': TextInput(attrs={
                'placeholder': "Тег клиента",
                'class': "form-control"
            })
        }

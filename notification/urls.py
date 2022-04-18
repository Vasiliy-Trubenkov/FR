from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_client', views.create_client, name='create_client'),
    path('client_edit/<int:pk>', views.ClientUpdateView.as_view(), name='edit_client'),
    path('client_delete/<int:pk>', views.ClientDeleteView.as_view(), name='delete_client'),
    path('create_mailing', views.create_mailing, name='create_mailing'),
    path('edit_mailing/<int:pk>', views.MailingUpdateView.as_view(), name='edit_mailing'),
    path('mailing_more/<int:pk>', views.MailingDetailView.as_view(), name='mailing_more'),
    path('delete_mailing/<int:pk>', views.MailingDeleteView.as_view(), name='delete_mailing'),
    path('directory', views.directory, name='directory'),
    path('mailing_statistic', views.mailing_statistic, name='mailing_statistic')
]

from django.urls import path
from . import views

urlpatterns = [
    path('purchase_ticket/', views.purchase_ticket, name='purchase_ticket'),
    path('ticket_success/', views.ticket_success, name='ticket_success'),
]

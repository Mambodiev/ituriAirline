
from django.contrib import admin
from django.urls import path
from django_filters.views import FilterView
from .filters import TicketFilter

from ticket import views

app_name = 'ticket'

from ticket.views import (
    # ticket_list,
    ticket_retrieve,
    ticket_create,
    ticket_update,
    ticket_delete
)

urlpatterns = [
    # path('', ticket_list),
    path('payment/', views.PaymentView.as_view(), name='payment'),
    path('summary/', views.TicketView.as_view(), name='summary'),
    path('increase-quantity/<pk>/',
         views.IncreaseQuantityView.as_view(), name='increase-quantity'),
    path('decrease-quantity/<pk>/',
         views.DecreaseQuantityView.as_view(), name='decrease-quantity'),
    path('remove-from-ticket/<pk>/',
         views.RemoveFromTicketView.as_view(), name='remove-from-ticket'),
    path('home',views.HomeView.as_view(), name='home'),
    path('',FilterView.as_view(
     filterset_class=TicketFilter,
     template_name = "ticket/ticket_list.html"
     ),
     name='ticket-list'),
    path('ticket/<int:pk>', views.TicketDetailView.as_view(), name='ticket-detail'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('tickets/<pk>/', ticket_retrieve),
    path('tickets/<pk>/edit/', ticket_update),
    path('tickets/<pk>/delete/', ticket_delete),
    path('add-ticket/', ticket_create),


] 
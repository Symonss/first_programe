from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from home import views, owners
from home.owners import AppointmentUpdate, Appointment2CreateView
from home.clients import ClientUpdate, AppointmentCreateView
from home.clients import AppointmentListView, CommentsListView


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('faqs/', views.faqs, name='faqs'),
    path('client/update/', ClientUpdate.as_view(), name='client_update'),
    path('owner/update/', owners.OwnerUpdate.as_view(), name='owner_update'),
    path('dashboard/<int:id>/', views.dashboard, name='dashboard'),
    path('Salon/<int:id>/', views.moreinfo, name='moreinfo'),
    path('Salon/payment/', views.clientPayment, name='clientPayment'),
    path('user/<int:id>/', views.user, name='user'),
    path('productsServices/', views.productsServices, name='productsServices'),
    path('staffClients/', views.staffClients, name='staffClients'),
    path('map/', views.map, name='map'),
    path('calendar/', views.calendar, name='calendar'),
    path('upgrade/', views.upgrade, name='upgrade'),
    path('upload/', views.upload, name='upload'),
    path('update_views/', views.update_views, name="update_views"),
    path('appointment/add/', AppointmentCreateView.as_view(),
         name='appointment_add'),
    path('special/appointment/add/',
         Appointment2CreateView.as_view(), name='appointment2_add'),
    path('salon/add/', owners.SalonCreateView.as_view(), name='salon_add'),
    path('client/dashboard', AppointmentListView.as_view(),
         name='client_dashboard'),
    path('dashboard/', views.AppointmentListView.as_view(), name='dashboard'),
    path('client/dashboard2', CommentsListView.as_view(),
         name='client_dashboard2'),
    path('appointment/<int:pk>/', views.appointment_detail,
         name='appointment_detail'),
    path('appointment/<pk>/accept/',
         views.appointment_accept, name='appointment_accept'),
    path('appointment/<pk>/reject/',
         views.appointment_reject, name='appointment_reject'),
    path('update/<int:pk>/', AppointmentUpdate.as_view(), name='a_update'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from home import views, owners
from home.owners import AppointmentUpdate, Appointment2CreateView
from home.clients import ClientUpdate, AppointmentCreateView
from home.clients import AppointmentListView, MiniDashboard
from home.clients import ReviewsListView, MyAppointments, MyReviews


urlpatterns = [
    path('', views.index, name='home'),
    path('salon/new/', owners.SalonCreateView.as_view(), name='new_salon'),
    path('salon/<slug:name>/', views.salon_details, name='salon_details'),
    path('api/v1/confirmation', views.confirmation, name='confirmation'),
    path('transaction/inprogress', views.transaction_progress, name='transaction_progress'),
    path('api/v1/validation', views.validation, name='validation'),
    path('mpesa', views.mpesa, name='mpesa'),
    path('current/registerd/salons', views.crs, name='crs'),
    path('about/', views.about, name='about'),
    path('faqs/', views.faqs, name='faqs'),
    path('add_salon', views.signup_steps, name='add_salon'),
    path('client/update/', ClientUpdate.as_view(), name='client_update'),
    path('owner/update/', owners.OwnerUpdate.as_view(), name='owner_update'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('preference/', views.preference, name='preference'),
    path('Salon/payment/', views.clientPayment, name='clientPayment'),
    # profile starts here
    path('dashboard/profile/', views.profile, name='profile'),
    # reviews starts here
    path('dashboard/reviews/', views.reviews, name='reviews'),
    # customers starts here
    path('dashboard/customers/', views.customers, name='customers'),
    # services starts here
    path('dashboard/services', views.services, name='services'),
    path('dashboard/services/new', views.service_new, name='service_new'),
    path('dashboard/service/<int:id>/edit',
         views.service_edit,
         name='service_edit'),
    path('dashboard/service/<int:id>/remove/',
         views.service_delete,
         name='service_delete'),
    # products starts here
    path('dashboard/products', views.products, name='products'),
    path('dashboard/products/new', views.product_new, name='product_new'),
    path('dashboard/product/<int:id>/edit',
         views.product_edit,
         name='product_edit'),
    path('dashboard/product/<int:id>/remove/',
         views.product_delete,
         name='product_delete'),
    # appointments starts here
    path('dashboard/appointments',
         views.appointments,
         name='dashboard_appointments'),
    path('appointment/update/<int:pk>/',
         AppointmentUpdate.as_view(),
         name='a_update'),
    path('dashboard/appointments/new/',
         views.dashboard_appointments_new,
         name='dashboard_appointments_new'),
    path('appointments/complete/<int:pk>/',
         views.appointment_complete,
         name='appointment_complete'),
    # staffs starts here
    path('dashboard/staffs/', views.staffs, name='staffs'),
    path('dashboard/staffs/new/', views.staff_new, name='staff_new'),
    path('dashboard/staff/<int:id>/edit', views.staff_edit, name='staff_edit'),
    path('dashboard/staff/<int:id>/remove/',
         views.staff_delete,
         name='staff_delete'),

    # salon images starts here
    path('dashboard/salon/images<slug:slug>',
         views.salon_images,
         name='salon_images'),
    path('dashboard/salon/select/images<slug:slug>/<int:id>',
         views.select_image,
         name='select_images'),
    path('user/profile', views.user_profile, name='user_profile'),

    path('upload/', views.upload, name='upload'),
    path('about/client/<int:pk>/',
         views.client_profile_for_salons,
         name='client_profile_for_salons'),

    #     client dashboard A.K.A Mini dashboard
    path('client/dashboard',
         AppointmentListView.as_view(),
         name='client_dashboard'),
    path('client/dashboard2',
         ReviewsListView.as_view(),
         name='client_dashboard2'),
    path('user/profile/', MiniDashboard.as_view(), name='mini_dashboard'),
    path('my/appointments', MyAppointments.as_view(), name='my_appointments'),
    path('my/reviews', MyReviews.as_view(), name='my_reviews'),
    #     end of client dashboard
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

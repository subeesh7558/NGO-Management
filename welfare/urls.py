
from django.urls import path, include
from welfare import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('causes/', views.causes, name='causes'),
    path('donate/', views.donate, name='donate'),
    path('gallery/', views.gallery, name='gallery'),
    path('event/', views.event, name='event'),
    path('contact/', views.contact, name='contact'),
    path('loginwelfare/', views.loginwelfare, name='loginwelfare'),
    path('login/', views.login, name='login'),
    path('reg/', views.reg, name='reg'),
    path('Registration/', views.Registration, name='Registration'),
    path('donation/',views.donation, name='donation'),


    # path('ngoo/', views.ngo, name="ngoo"),
    # path('ngo/', include('ngo.urls')),




    path('Admin_index', views.Admin_index, name='Admin_index'),
    path('Admin_doner_det/', views.Admin_doner_det, name='Admin_doner_det'),
    path('Admin_ngo_det/', views.Admin_ngo_det, name='Admin_ngo_det'),
    path('Admin_nofification/', views.Admin_nofification, name='Admin_nofification'),
    path('Admin_nofification/', views.Admin_nofification, name='Admin_nofification'),
    path('Admin_reject/<int:id>', views.Admin_reject, name='Admin_reject'),
    path('Admin_approve/<int:id>', views.Admin_approve, name='Admin_approve'),
    path('Admin_Msg_doner/', views.Admin_Msg_doner, name='Admin_Msg_doner'),
    path('Admin_Msg_ngo/', views.Admin_Msg_ngo, name='Admin_Msg_ngo'),

    path('Admin_logout/',views.Admin_logout, name='Admin_logout'),
    path('Ngo_logout/',views.Ngo_logout, name='Ngo_logout'),

    path('Ngo_index/', views.Ngo_index, name='Ngo_index'),
    path('Ngo_No_Card/', views.Ngo_No_Card, name='Ngo_No_Card'),
    path('Ngo_doner_det/', views.Ngo_doner_det, name='Ngo_doner_det'),
    path('Ngo_nofification/', views.Ngo_nofification, name='Ngo_nofification'),
    path('Ngo_reject/<int:id>', views.Ngo_reject, name='Ngo_reject'),
    path('Ngo_approve/<int:id>', views.Ngo_approve, name='Ngo_approve'),
    path('Ngo_donation_history/', views.Ngo_donation_history, name='Ngo_donation_history'),
    path('Ngo_admin_messages/', views.Ngo_admin_messages, name='Ngo_admin_messages'),




    path('Donar_index/', views.Donar_index, name='Donar_index'),
    path('Donar_donation/', views.Donar_donation, name='Donar_donation'),
    path('Donar_logout/',views.Donar_logout, name='Donar_logout'),
    path('Donar_donation_registration/',views.Donar_donation_registration, name='Donar_donation_registration'),
    path('Donar_donation_det/',views.Donar_donation_det, name='Donar_donation_det'),
    path('Doner_req_det/', views.Doner_req_det, name='Doner_req_det'),
    path('Doner_admin_message/', views.Doner_admin_message, name='Doner_admin_message'),


    
]

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
    path('reg_rest/', views.reg_rest, name='reg_rest'),
    path('Registration/', views.Registration, name='Registration'),
    path('Registration2/', views.Registration2, name='Registration2'),
    path('donation/',views.donation, name='donation'),
    path('Forgot_password/',views.Forgot_password, name='Forgot_password'),


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
    path('Admin_No_Card/', views.Admin_No_Card, name='Admin_No_Card'),
    path('Admin_Notification_des_Card/', views.Admin_Notification_des_Card, name='Admin_Notification_des_Card'),
    path('Admin_ngo_messages/', views.Admin_ngo_messages, name='Admin_ngo_messages'),
    path('Admin_donar_messages/', views.Admin_donar_messages, name='Admin_donar_messages'),
    path('Admin_donar_donation_history/', views.Admin_donar_donation_history, name='Admin_donar_donation_history'),
    path('Admin_restaurent_req_food_det/', views.Admin_restaurent_req_food_det, name='Admin_restaurent_req_food_det'),
    path('Admin_reply_restaurent/<int:id>', views.Admin_reply_restaurent, name='Admin_reply_restaurent'),
    path('Admin_reason_restaurent/<int:id>', views.Admin_reason_restaurent, name='Admin_reason_restaurent'),
    path('Admin_Accountsett/', views.Admin_Accountsett, name='Admin_Accountsett'),


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
    path('Ngo_admin_messages_replay/<int:id>', views.Ngo_admin_messages_replay, name='Ngo_admin_messages_replay'),
    path('Ngo_Admin_res_approved_food_det/', views.Ngo_Admin_res_approved_food_det, name='Ngo_Admin_res_approved_food_det'),
    path('Ngo_Accsetting/', views.Ngo_Accsetting, name='Ngo_Accsetting'),
    path('Ngo_Changepwd/<int:id>', views.Ngo_Changepwd, name='Ngo_Changepwd'),




    path('Donar_index/', views.Donar_index, name='Donar_index'),
    path('Donar_donation/', views.Donar_donation, name='Donar_donation'),
    path('Donar_logout/',views.Donar_logout, name='Donar_logout'),
    path('Donar_donation_registration/',views.Donar_donation_registration, name='Donar_donation_registration'),
    path('Donar_donation_det/',views.Donar_donation_det, name='Donar_donation_det'),
    path('Doner_req_det/', views.Doner_req_det, name='Doner_req_det'),
    path('Doner_admin_message/', views.Doner_admin_message, name='Doner_admin_message'),
    path('Donar_admin_messages_replay/<int:id>', views.Donar_admin_messages_replay, name='Donar_admin_messages_replay'),
    path('Doner_Accsetting/', views.Doner_Accsetting, name='Doner_Accsetting'),
    path('Doner_Changepwd/<int:id>', views.Doner_Changepwd, name='Doner_Changepwd'),




    path('Restaurant_index/', views.Restaurant_index, name='Restaurant_index'),
    path('Restaurant_logout/',views.Restaurant_logout, name='Restaurant_logout'),
    path('Restaurant_req_food/',views.Restaurant_req_food, name='Restaurant_req_food'),
    path('Restaurant_Card/',views.Restaurant_Card, name='Restaurant_Card'),
    path('Request_res_food/',views.Request_res_food, name='Request_res_food'),
    path('restaurent_requested_food_det/',views.restaurent_requested_food_det, name='restaurent_requested_food_det'),
    path('Restaurent_Admin_messages/',views.Restaurent_Admin_messages, name='Restaurent_Admin_messages'),
    path('Restaurent_Accsetting/', views.Restaurent_Accsetting, name='Restaurent_Accsetting'),
    path('Restaurent_Changepwd/<int:id>', views.Restaurent_Changepwd, name='Restaurent_Changepwd'),
]
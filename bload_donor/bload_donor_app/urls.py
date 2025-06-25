from django.urls import path
from . import views 
from .tokens import donor_password_reset_token

urlpatterns = [
    # Homepage and role selection
    path('', views.index, name='index'),
    path('role/', views.role_selection, name='role_selection'),

    # Collector authentication and registration
    
    path('register_collector/', views.register_collector, name='register_collector'),
    #collector reset password
    path('collector/reset/<uidb64>/<token>/', views.collector_reset_password, name='collector_reset_password'),
    path('change-password/', views.change_password, name='change_password'),
    path('collector_login/', views.collector_login, name='collector_login'), 


    # Donor registration 3-step flow
    path('register_donor/', views.register_donor, name='register_donor'),  # Step 1
    path('credential/', views.credential, name='credential'),  # Step 2
    path('complete/', views.complete, name='complete'),  # Step 3
    # Donor login
    path('donor_login/', views.donor_login, name='donor_login'),
    # Dashboard/profile pages
    path('donor/', views.donor, name='donor'),
    #schedule appointment
    path('schedule_appointment/', views.schedule_appointment, name='schedule_appointment'),
    path('collector/', views.collector, name='collector'),
    path('schedule-drive/', views.schedule_drive, name='schedule_drive'),
    path('collector/send-notification/', views.send_mass_notification, name='send_notification'),
    path('collector/schedule-drive/', views.schedule_drive, name='schedule_drive'),
    path('collector/edit-drive/<int:drive_id>/', views.edit_drive, name='edit_drive'),
    path('collector/delete-drive/<int:drive_id>/', views.delete_drive, name='delete_drive'),
    path('get-drives/', views.get_drives_by_location, name='get_drives_by_location'),
    path('drive/<int:drive_id>/message/', views.send_drive_message, name='send_drive_message'),


    # path('send-notification/', views.send_mass_notification, name='send_notification'),
    path('Profile/', views.Profile, name='Profile'),

    # Settings pages
    path('settings_donor/', views.settingsdonor, name='settings'),
    path('settings_collector/', views.settingscolle, name='settingscolle'),

    # Password reset endpoints
    # path('reset_donor_password/', views.donor_password_reset_request, name='donor_password_reset_request'),
    path('reset_collector_password/', views.collector_password_reset_request, name='collector_password_reset_request'),
   
    # ========================================logout as for donor and collector============================
    path('donor/logout/', views.donor_logout, name='donor_logout'),
    path('collector/logout/', views.collector_logout, name='collector_logout'),

    #==================================report for collector dashboard=======================================
    path('collector/reports/', views.generate_reports, name='generate_reports'),
    path('collector/reports/export/csv/', views.export_report_csv, name='export_report_csv'),
    path('collector/reports/export/pdf/', views.export_report_pdf, name='export_report_pdf'),

    # ==========================for resetting the donor password using forget password option==============
    # path('donor/forgot-password/', views.donor_forget_reset, name='donor_forget_reset'),
    # path('donor/reset-password/<str:token>/', views.reset_donor_password, name='reset_donor_password'),
    #============================ testmonial ================================================
    path('submit-testimonial/', views.submit_testimonial, name='submit_testimonial'),
    path('testimonial-thanks/', views.testimonial_thanks, name='testimonial_thanks'),
    #================donor additional details as per collect dashboard=================
    path('collector/donor/<int:donor_id>/', views.donor_detail_view, name='donor_detail'),
    path('collector/donor/<int:donor_id>/send-message/', views.send_message_form, name='send_message'),

    # ==============================donor forget passwor final========================================
    path('donor-forget-password/', views.donor_forget_request, name='donor_forget_request'),
    path('donor-forget-password/done/', views.donor_forget_done, name='donor_forget_done'),
    path('donor-forget-password-confirm/<uidb64>/<token>/', views.donor_forget_confirm, name='donor_forget_confirm'),

    #=====================coleector forget password final ===================================
    path('collector-forget-password/', views.collector_forget_request, name='collector_forget_request'),
    path('collector-forget-password-confirm/<uidb64>/<token>/', views.collector_forget_confirm, name='collector_forget_confirm'),
]



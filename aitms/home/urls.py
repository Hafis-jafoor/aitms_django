from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.index_contact, name='home'),
    # path('', views.Admission_councellor, name='home'),
    path('', views.index, name='home'),
    path('about_overview/', views.about_overview, name='about_overview'),
    path('vision_mission/', views.vision_mission, name='vision_mission'),
    path('leadershipteam/', views.leadershipteam, name='leadershipteam'),
    path('ranking_recognition/', views.ranking_recognition, name='ranking_recognition'),
    path('collaborations/', views.collaborations, name='collaborations'),
    path('blogs/', views.blogs, name='blogs'),
    path('Social_responsibilities/', views.Social_responsibilities, name='Social_responsibilities'),
    path('admissions_overview/', views.admissions_overview, name='admissions_overview'),
    path('ug_programs/', views.ug_programs, name='ug_programs'),
    path('pg_programs/', views.pg_programs, name='pg_programs'),
    path('diploma_programs/', views.diploma_programs, name='diploma_programs'),
    path('other_short_programs/', views.other_short_programs, name='other_short_programs'),
    path('scholorship/', views.scholorship, name='scholorship'),
    path('career_guidance/', views.career_guidance, name='career_guidance'),
    path('campuses/', views.campuses, name='campuses'),
    path('learning_methodology/', views.learning_methodology, name='learning_methodology'),
    path('library_recourse_center/', views.library_recourse_center, name='library_recourse_center'),
    path('allied_departments/', views.allied_departments, name='allied_departments'),
    path('sports_recreation/', views.sports_recreation, name='sports_recreation'),
    path('hostal_facilities/', views.hostal_facilities, name='hostal_facilities'),
    path('industry_visits/', views.industry_visits, name='industry_visits'),
    path('placements_overview/', views.placements_overview, name='placements_overview'),
    path('placement_training/', views.placement_training, name='placement_training'),
    path('job_fairs_events/', views.job_fairs_events, name='job_fairs_events'),
    path('current_offers/', views.current_offers, name='current_offers'),
    # path('current_offers/', views.Admission_councellor, name='current_offers'),
    path('internship_opportunities/', views.internship_opportunities, name='internship_opportunities'),
    path('part_time_opportunities/', views.part_time_opportunities, name='part_time_opportunities'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('parscore/', views.parscore, name='parscore'),  
]

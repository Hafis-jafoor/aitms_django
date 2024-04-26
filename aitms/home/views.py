from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about_overview(request):
    return render(request, 'about_overview.html')
    
def vision_mission(request):
    return render(request, 'vision_mission.html')

def leadershipteam(request):
    return render(request, 'leadershipteam.html')

def ranking_recognition(request):
    return render(request, 'ranking_recognition.html')

def collaborations(request):
    return render(request, 'collaborations.html')

def blogs(request):
    return render(request, 'blogs.html')

def Social_responsibilities(request):
    return render(request, 'Social_responsibilities.html')

def admissions_overview(request):
    return render(request, 'admissions_overview.html')

def ug_programs(request):
    return render(request, 'ug_programs.html')

def pg_programs(request):
    return render(request, 'pg_programs.html')

def diploma_programs(request):
    return render(request, 'diploma_programs.html')

def other_short_programs(request):
    return render(request, 'other_short_programs.html')

def scholorship(request):
    return render(request, 'scholorship.html')

def career_guidance(request):
    return render(request, 'career_guidance.html')

def campuses(request):
    return render(request, 'campuses.html')

def learning_methodology(request):
    return render(request, 'learning_methodology.html')

def library_recourse_center(request):
    return render(request, 'library_&_recourse_center.html')

def allied_departments(request):
    return render(request, 'allied_departments.html')

def sports_recreation(request):
    return render(request, 'sports_&_recreation.html')

def hostal_facilities(request):
    return render(request, 'hostal_facilities.html')

def industry_visits(request):
    return render(request, 'industry_visits.html')

def placements_overview(request):
    return render(request, 'placements_overview.html')

def placement_training(request):
    return render(request, 'placement_training.html')

def job_fairs_events(request):
    return render(request, 'job_fairs_&_events.html')

def current_offers(request):
    return render(request, 'current_offers.html')

def internship_opportunities(request):
    return render(request, 'internship_opportunities.html')

def part_time_opportunities(request):
    return render(request, 'part_time_opportunities.html')

def testimonials(request):
    return render(request, 'testimonials.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def parscore(request):
    return render(request, 'parscore.html')

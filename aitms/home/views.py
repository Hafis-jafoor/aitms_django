from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about_overview(request):
    return HttpResponse("about_overview")
    
def vision_mission(request):
    return HttpResponse("vision_mission")

def leadershipteam(request):
    return HttpResponse("leadershipteam")

def ranking_recognition(request):
    return HttpResponse("ranking_recognition")

def collaborations(request):
    return HttpResponse("collaborations")

def blogs(request):
    return HttpResponse("blogs")

def Social_responsibilities(request):
    return HttpResponse("Social_responsibilities")

def admissions_overview(request):
    return HttpResponse("admissions_overview")

def ug_programs(request):
    return HttpResponse("ug_programs")

def pg_programs(request):
    return HttpResponse("pg_programs")

def diploma_programs(request):
    return HttpResponse("diploma_programs")

def other_short_programs(request):
    return HttpResponse("other_short_programs")

def scholorship(request):
    return HttpResponse("scholorship")

def career_guidance(request):
    return HttpResponse("career_guidance")

def campuses(request):
    return HttpResponse("campuses")

def learning_methodology(request):
    return HttpResponse("learning_methodology")

def library_recourse_center(request):
    return HttpResponse("library_&_recourse_center")

def allied_departments(request):
    return HttpResponse("allied_departments")

def sports_recreation(request):
    return HttpResponse("sports_&_recreation")

def hostal_facilities(request):
    return HttpResponse("hostal_facilities")

def industry_visits(request):
    return HttpResponse("industry_visits")

def placements_overview(request):
    return HttpResponse("placements_overview")

def placement_training(request):
    return HttpResponse("placement_training")

def job_fairs_events(request):
    return HttpResponse("job_fairs_&_events")

def current_offers(request):
    return HttpResponse("current_offers")

def internship_opportunities(request):
    return HttpResponse("internship_opportunities")

def part_time_opportunities(request):
    return HttpResponse("current_part_time_opportunitiesoffers")

def scholorship(request):
    return HttpResponse("scholorship")

def contact_us(request):
    return HttpResponse("contact_us")

def parscore(request):
    return HttpResponse("parscore")

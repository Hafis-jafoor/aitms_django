from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .models import Enquiry_contacts, Vistor_contacts, Parscore, Admissioncouncellor
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
# def index(request):
#     return render(request, 'index.html')

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

# def current_offers(request):
#     return render(request, 'current_offers.html')

def internship_opportunities(request):
    return render(request, 'internship_opportunities.html')

def part_time_opportunities(request):
    return render(request, 'part_time_opportunities.html')

def testimonials(request):
    return render(request, 'testimonials.html')

# def contact_us(request):
#     return render(request, 'contact_us.html')

# def parscore(request):
#     return render(request, 'parscore.html')

def contact_us(request):
    if request.method == 'POST':
        contact_name = request.POST.get('name2')
        contact_email = request.POST.get('email2')
        contact_phone = request.POST.get('phone2')
        contact_subject = request.POST.get('subject2')
        contact_message = request.POST.get('message2')

        # Check if the email already exists
        if Enquiry_contacts.objects.filter(contact_email=contact_email).exists():
            messages.error(request, 'Email already exists(mail has been registered already,use another valid email).')
            return render(request, 'contact_us.html', {'name': contact_name, 'email': contact_email, 'phone': contact_phone, 'subject': contact_subject, 'message': contact_message})

        # Create and save the contact object
        contact = Enquiry_contacts.objects.create(
            contact_name=contact_name,
            contact_email=contact_email,
            contact_phone=contact_phone,
            contact_subject=contact_subject,
            contact_message=contact_message,
        )

        # Send email
        send_mail(
            'Enquiry Contact Form Submission of Aitms',
            f'Name: {contact_name}\nEmail: {contact_email}\nPhone: {contact_phone}\nSubject: {contact_subject}\nMessage: {contact_message}',
            contact_email,  # From email (user's email address)
            # settings.EMAIL_HOST_USER,  # From email (configured in settings.py)
            ['sticknobillshafis@gmail.com'],  # To email
            fail_silently=False,
        )

        messages.success(request, 'Your message has been stored successfully .')
        return redirect('contact_us')
    return render(request, 'contact_us.html')

def index_contact(request):
    if request.method == 'POST':
        contact_name = request.POST.get('name')
        contact_email = request.POST.get('email')
        contact_phone = request.POST.get('phone')
        contact_subject = request.POST.get('subject')
        contact_message = request.POST.get('message')

        # Check if the email already exists
        # if Vistor_contacts.objects.filter(contact_email=contact_email).exists():
        #     messages.error(request, 'Email already exists(mail has been registered already,use another valid email).')
        #     return render(request, 'index.html', {'name': contact_name, 'email': contact_email, 'phone': contact_phone, 'subject': contact_subject, 'message': contact_message})

        # Create and save the contact object
        contact = Vistor_contacts.objects.create(
            contact_name=contact_name,
            contact_email=contact_email,
            contact_phone=contact_phone,
            contact_subject=contact_subject,
            contact_message=contact_message,
        )

        # Send email
        send_mail(
            'Vistor Contact Form Submission of Aitms',
            f'Name: {contact_name}\nEmail: {contact_email}\nPhone: {contact_phone}\nSubject: {contact_subject}\nMessage: {contact_message}',
            contact_email,  # From email (user's email address)
            # settings.EMAIL_HOST_USER,  # From email (configured in settings.py)
            ['sticknobillshafis@gmail.com'],  # To email
            fail_silently=False,
        )

        messages.success(request, 'Your message has been stored successfully|Click the Close Button .')
        return redirect('home')
    return render(request, 'index.html')

def parscore(request):
    if request.method == 'POST':
        Parscore_student_name = request.POST.get('name3')
        Parscore_school_name = request.POST.get('sname')
        Parscore_sector = request.POST.get('select1')
        Parscore_phone = request.POST.get('phone3')
        Parscore_email = request.POST.get('email3')
        Parscore_location = request.POST.get('select2')
        Parscore_career = request.POST.get('select3')
        Parscore_career_other = request.POST.get('otherInput')

        # Check if the email already exists
        if Parscore.objects.filter(Parscore_email=Parscore_email).exists():
            messages.error(request, 'Email already exists(mail has been registered already,use another valid email).')
            return render(request, 'parscore.html', {'name3': Parscore_student_name, 'sname': Parscore_school_name, 
                                                     'select1': Parscore_sector, 'phone3': Parscore_phone, 'email3': Parscore_email, 
                                                     'select2': Parscore_location, 'select3': Parscore_career, 
                                                     'otherInput': Parscore_career_other})

        # Create and save the contact object
        parscore = Parscore.objects.create(
            Parscore_student_name=Parscore_student_name,
            Parscore_school_name=Parscore_school_name,
            Parscore_sector=Parscore_sector,
            Parscore_phone=Parscore_phone,
            Parscore_email=Parscore_email,
            Parscore_location=Parscore_location,
            Parscore_career=Parscore_career,
            Parscore_career_other=Parscore_career_other,
        )

        # Send email
        send_mail(
            'Parscore scholorship Form Submission of Aitms',
            f'StudentName: {Parscore_student_name}\nSchoolName: {Parscore_school_name}\nSector: {Parscore_sector}\nPhone: {Parscore_phone}\nEmail: {Parscore_email}\nLocation: {Parscore_location}\ncareer: {Parscore_career}\ncareeer_other: {Parscore_career_other}',
            Parscore_email,  # From email (user's email address)
            # settings.EMAIL_HOST_USER,  # From email (configured in settings.py)
            ['sticknobillshafis@gmail.com'],  # To email
            fail_silently=False,
        )

        messages.success(request, 'Your message has been stored successfully .')
        return redirect('parscore')
    return render(request, 'parscore.html')

def Admission_councellor(request):
    if request.method == 'POST':
        name = request.POST.get('name1')
        email = request.POST.get('email1')
        phone = request.POST.get('phone1')
        message = request.POST.get('message1')
        resume = request.FILES.get('resume1')  # Use request.FILES to get the uploaded file

        # Check if the email already exists
        if Admissioncouncellor.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists (mail has been registered already, use another valid email).')
            return render(request, 'current_offers.html', {'name1': name, 'email1': email, 
                                                            'phone1': phone, 'message1': message, 'resume1': resume})

        # Create and save the contact object
        Admissioncouncellors = Admissioncouncellor.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message,
            resume=resume,
        )

        # Send email
        send_mail(
            'Admission Councellors Form Submission of Aitms',
            f'name: {name}\nemail: {email}\nphone: {phone}\nmessage: {message}\nresume: {resume}',
            email,  # From email (user's email address)
            # settings.EMAIL_HOST_USER,  # From email (configured in settings.py)
            ['sticknobillshafis@gmail.com'],  # To email
            fail_silently=False,
        )

        messages.success(request, 'Your message has been stored successfully.')
        return redirect('current_offers')
    return render(request, 'current_offers.html')



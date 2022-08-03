from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.db.models import F
from django.views import generic
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from .forms import *
from . import models


def home_page(request):
    return render(request, "home_page.html")


def login_user(request):
    form = UserLoginForm(data=request.POST)
    if request.POST.get('username') is None:
        return render(request, "login_page.html", context={'wrong': False, 'form': UserLoginForm()})
    if not form.is_valid():
        return render(request, "login_page.html", context={'wrong': False, 'form': form})
    c = form.cleaned_data
    username = c['username']
    password = c['password']
    user = authenticate(request, username=username, password=password)
    if user is None:
        return render(request, "login_page.html", context={'wrong': True, 'form': form})
    else:
        login(request, user)
        return redirect('home')


def register_user(request):
    form = UserRegisterForm(data=request.POST)
    if request.POST.get('username') is None:
        return render(request, "register_page.html", context={'form': UserRegisterForm()})
    if not form.is_valid():
        return render(request, "register_page.html", context={'form': form})
    else:
        c = form.cleaned_data
        u = c['username']
        f = c['firstname']
        l = c['lastname']
        e = c['email']
        p1 = c['password1']
        p2 = c['password2']
        passwords_not_match = p1!=p2
        user_exists = User.objects.filter(username=u).exists()
        if passwords_not_match or user_exists:
            return render(request, "register_page.html",
                context={'passwords_not_match': passwords_not_match, 'user_exists': user_exists,
                         'form': form})
        account = models.Account()
        user = User(username=u, email=e, first_name=f, last_name=l, account=account)
        user.set_password(p1)
        user.save()
        account.save()
        return redirect('login')


def logout_user(request):
    try:
        logout(request)
    except Exception:
        pass
    return redirect('home')


def send_feedback(request):
    form = FeedbackForm(data=request.POST)
    if request.POST.get('title') is None:
        return render(request, "feedback_page.html", context={'form': FeedbackForm()})
    if not form.is_valid():
        return render(request, "feedback_page.html", context={'form': form})
    c = form.cleaned_data
    title = c['title']
    text = c['text']
    e = c['email']
    text += "\n\n"+e
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [settings.EMAIL_RECIPIENT]
    send_mail(subject=title, message=text, from_email=email_from, recipient_list=recipient_list)
    return redirect('feedbackSent')


def feedback_sent(request):
    return render(request, "feedback_sent_page.html")


@login_required()
def show_profile(request):
    return render(request, "profile_page.html")


@login_required()
def edit_profile(request):
    if request.POST.get('firstname') is None:
        return render(request, "setting_page.html", context={'form': UserProfileSettingForm(initial={
            'firstname': request.user.first_name,
            'lastname': request.user.last_name,
            'bio': request.user.account.bio,
            'gender': request.user.account.gender
        })})
    form = UserProfileSettingForm(data=request.POST, files=request.FILES, instance=request.user.account)
    if form.is_valid():
        form.save()
    c = form.cleaned_data
    firstname = c['firstname']
    lastname = c['lastname']
    q = User.objects.filter(username=request.user.username)
    if firstname!='':
        q.update(first_name=firstname)
    if lastname!='':
        q.update(last_name=lastname)
    account = models.Account.objects.filter(user=q.first())
    account.update(bio=c['bio'])
    account.update(gender=c['gender'])
    return redirect('profile')


@login_required()
def show_panel(request):
    return render(request, "panel_page.html")


@login_required()
def new_course(request):
    if request.user.is_superuser:
        form = CourseRegisterForm(data=request.POST)
        if not form.is_valid():
            if request.POST.get('department') is None:
                return render(request, "course_register_page.html", context={'form': CourseRegisterForm()})
            return render(request, "course_register_page.html", context={'form': form})
        c = form.cleaned_data
        department = c['department']
        name = c['name']
        course_number = c['course_number']
        group_number = c['group_number']
        teacher = c['teacher']
        start_time = c['start_time']
        end_time = c['end_time']
        first_day = c['first_day']
        second_day = c['second_day']
        valid = True
        if end_time<start_time:
            valid = False
        if second_day!='7' and second_day<=first_day:
            valid = False
        if not valid:
            return render(request, "course_register_page.html", context={'form': form})
        models.Course.objects.create(
            department=department,
            name=name,
            course_number=course_number,
            group_number=group_number,
            teacher=teacher,
            start_time=start_time,
            end_time=end_time,
            first_day=first_day,
            second_day=second_day
        )
        return redirect('panel')
    else:
        return redirect('panel')


@login_required()
def show_all_courses(request):
    return render(request, "courses_page.html", context={'course_list': models.Course.objects.all()})
